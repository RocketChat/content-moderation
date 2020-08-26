# Train your own model!
1. We are using [PyTorch's resnet18 notebook](https://github.com/RocketChat/content-moderation/blob/master/server/notebooks/PyTorch/moderation_v1(resnet18).ipynb) in our official Flask App.
2. To open the [notebook](https://github.com/RocketChat/content-moderation/blob/master/server/notebooks/PyTorch/moderation_v1(resnet18).ipynb) you can use the [Google Colab's link](https://colab.research.google.com/github/shreyanshtomar/moderation/blob/shreyansh_dev/server/notebooks/PyTorch/moderation_v1(resnet18).ipynb) to directly open the Notebook or Download it and open it from any Cloud Service Providers like AWS, GCP, etc. or you can run it locally too.
3. To add data you can use either of the below mentioned options:<br>
  a. [PyDrive Reference](https://pythonhosted.org/PyDrive/)<br>[Google Drive API reference](https://developers.google.com/drive/v3/reference/)

    ```# Import PyDrive and associated libraries.
    # This only needs to be done once per notebook.
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive
    from google.colab import auth
    from oauth2client.client import GoogleCredentials

    # Authenticate and create the PyDrive client.
    # This only needs to be done once per notebook.
    auth.authenticate_user()
    gauth = GoogleAuth()
    gauth.credentials = GoogleCredentials.get_application_default()
    drive = GoogleDrive(gauth)

    # Download a file based on its file ID.
    #
    # A file ID looks like: laggVyWshwcyP6kEI-y_W3P8D26sz
    file_id = 'REPLACE_WITH_YOUR_FILE_ID'
    downloaded = drive.CreateFile({'id': file_id})
    print('Downloaded content "{}"'.format(downloaded.GetContentString()))
    ```
  b. Open files from Google Drive(Using Google Colab's GUI) & Copy them to Colab's File System.<br>
  The example below shows how to mount your Google Drive in your virtual machine using an authorization code.<br>
  ```from google.colab import drive
    drive.mount('/gdrive')
    %cd /gdrive
  ```
  c. Open files from your local file system <br>
   files.upload returns a dictionary of the files which were uploaded. The dictionary is keyed by the file name, the value is the data which was uploaded.
   ```from google.colab import files

      uploaded = files.upload()

      for fn in uploaded.keys():
        print('User uploaded file "{name}" with length {length} bytes'.format(name=fn, length=len(uploaded[fn])))
   ```
   d. If you want to use kaggle data in Colab you refer to this [link](https://www.kaggle.com/general/74235).
   
If files you have are zipped then you can use `!unzip file.zip` to unzip them in Colab.
The dataset should have the following directory structure:<br>
For training images: /content/train/<br>
For test images: /content/test/<br>
Now, that you have your data and Run all the cells after the heading Importing Library and Data. (Ctrl+F10).<br>
After all cells are completed with execution. In the Google Colab's /content/ directory there will be a resnet18_checkpoint.pth file generated. You can replace it with [resnet18_checkpoint.pth](https://github.com/RocketChat/content-moderation/blob/master/server/resnet18_checkpoint.pth) and run the Flask App again.




