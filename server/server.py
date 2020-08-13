from __future__ import print_function
import torch
import torch.functional as F
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torchvision import datasets, models, transforms
#from service_streamer import ThreadedStreamer

import copy    
import glob
import io
from io import open
import json
from pathlib import Path
import time
import requests

import re
import base64
from PIL import Image
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

RC_UUID = os.getenv('RC_UUID')
RC_TOKEN = os.getenv('RC_TOKEN')

#Automatically detects if the device is CUDA enabled to run GPU inferences.
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
device_avail = torch.cuda.is_available()
class_index = {0: 'nsfw', 1: 'sfw'}
net = models.resnet18(pretrained=True)
net = net.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.0001, momentum=0.9)

num_ftrs = net.fc.in_features
net.fc = nn.Linear(num_ftrs, 128)
net.fc = net.fc.to(device)

path = Path('resnet18_checkpoint.pth') #Path to the checkpoint(weight)

#Preparing model for evaluation based on device's capability
if not device_avail:
    print ('Model loaded & Inferencing on CPU...')
    net.load_state_dict(torch.load(path, map_location=torch.device('cpu')))
else:
    print ('Model loaded & Inferencing on GPU...')
    net.load_state_dict(torch.load(path))
print('*'*80)

#Evaluation mode
net.eval()

#Preprocess Image
def transform_image(image_bytes):
    my_transforms = transforms.Compose([transforms.Resize(255),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485, 0.456, 0.406],
                                            [0.229, 0.224, 0.225])])
    image = Image.open(image_bytes)
    return my_transforms(image).unsqueeze(0)

def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes).to(device)
    outputs = net.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = y_hat.item()
    return class_index[predicted_idx]

@app.route('/', methods=['GET'])
def root():
    return jsonify({'msg' : 'Try POSTing to the /predict endpoint with an RGB image attachment'})

# If there was an error processing image URLs, continue processing the rest of the images.
# If one of the image is NOT appropriate, return nsfw
# if all the images are appropriate, but had few errors processing other image, respond with error message with status code 500
# if all images successfully processed and are all appropriate, return sfw
@app.route('/predict', methods=['POST'])
def predict():
    # we will get the file from the request
    start_time = time.time()
    payload = request.get_json()
    error = {}

    for imgUrl in payload['url']:
        print('Retreiving Image...\n {}'.format(imgUrl))
        try:
            headers = {'x-user-id': RC_UUID,'x-auth-token': RC_TOKEN}
            response = requests.get(imgUrl, stream = True, headers = headers)
            
            fileType = response.headers['content-type']
            print(fileType)
            if response.status_code == 200 and fileType == ('image/jpeg' or 'image/png'):
                class_name = get_prediction(io.BytesIO(response.content))
            elif(fileType == ('image/jpeg' or 'image/png')):
                print('ERROR: Error while downloading image. Got status code {}.'.format(response.status_code))
                error = {'error':'Unexpected error encountered.'}
            else:
                print('ERROR: Error while downloading image. Got status code {}.'.format(response.status_code))
                error = {'error':'Unexpected error encountered.'}
                continue
        except Exception as ex:
            print('ERROR: {}'.format(ex))
            error = {'error':'Unexpected error encountered.'}
            continue

        end_time = time.time()
        totalTime = end_time-start_time
        print('Time - {}s'.format(totalTime))
        print('-'*80)

        if(fileType == ('image/jpeg' or 'image/png') and class_name == 'nsfw'):
            break

    if(fileType == ('image/jpeg' or 'image/png')):
        if class_name == 'nsfw' or not error:
            print({'classification': class_name})
            return jsonify({'classification': class_name})
        else:
            return jsonify(error), 500
    else:
        return jsonify(error), 500

if __name__ == '__main__':
    app.run(debug=True)
