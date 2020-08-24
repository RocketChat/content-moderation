# Content Moderation

Due to interactions between large communities among different channels in Rocket Chat, there was a need for support of an optional moderation service for offensive content. The service as of now is limited to image & links moderation which means if someone sends an offensive image or link to Rocket Chat app and the app along with server is deployed and configured then the image will be blocked but not videos.
The dockerised moderation service can be deployed to any server easily since all the major Cloud Providers such as AWS, GCP, Azure, IBM Cloud, etc. provides support to Docker.

![ezgif com-optimize](https://user-images.githubusercontent.com/18248623/89886718-babcff80-dbea-11ea-9c19-afee96f9aff1.gif)


## Quick start for code developers
Prerequisites:

* [Rocket.Chat-Deploy](https://docs.rocket.chat/apps-development/getting-started#installation)<br>
```npm install -g @rocket.chat/apps-cli```
* [Docker](https://docs.docker.com/get-docker/)
> Depending on the installation & machine while running docker commands you may want to use 'sudo' if you encounter any errors.
1. Open a Command Line and execute the following code.
```sh
git clone https://github.com/RocketChat/content-moderation.git
cd content-moderation
docker-compose up -d // This will launch a Rocket Chat Instance
```
2. Open Rocket.Chat instance ( http://127.0.0.1:3000 ) and Go through the Rocket.Chat initial setup. Remember
user-name and password for future use (we will also need it in later steps).
3. Generate Personal Access Tokens `My Account -> Personal Access Tokens -> Add `(You can either ignore or not ignore 2 Factor Authentication)
Copy User-ID & Token for future use.
4. From Rocket Chat open Administration -> General -> Apps and make sure the following options are enabled:
 - Enable App development mode 
 - Enable the App Framework
5. For Rocket.Chat [Content-Moderation-App](https://github.com/RocketChat/Apps.Moderation) installation follow steps
mentioned [here](https://github.com/RocketChat/Apps.Moderation/blob/master/README.md)

> After deployment let's configure Content Moderation App so that app can help in posting images to the hosted moderation-service to make predictions and
block offensive images/links.<br>
In our case:<br>
6. Administration -> Apps -> Content Moderation.<br>
'Rocket Chat host URL': http://rocket-chat:3000 &  'Content Moderation App Host URL': http://moderation-api:5000/predict in
Content Moderation App's Setting.<br>
Now, Let's deploy our service!!<br>
7. Edit [docker-compose-server.yml](https://github.com/RocketChat/content-moderation/blob/master/docker-compose-server.yml) in your local content-moderation directory.
& change the following
parameters:<br>
  a. [RC_UUID](https://github.com/RocketChat/content-moderation/blob/fa05ae92ca6497db6fca6558e2ff55ddc00c1543/docker-compose-server.yml#L13) <br>
  b. [RC_TOKEN](https://github.com/RocketChat/content-moderation/blob/fa05ae92ca6497db6fca6558e2ff55ddc00c1543/docker-compose-server.yml#L14)<br>
  We copied them in previous step.
```sh
cd .. # Make sure you're in moderation directory
docker-compose -f docker-compose-server.yml up -d
```
 ## Everything is configured now. We can now test the app!!.
 Try posting an offensive image in one of the channels & it should get blocked!
 
 To see the **logs** generated:
 ```sh
 docker logs moderation_rocketchat_1
 docker logs moderation_api_1
 ```
 ### Note
 The Machine Learning model currently recognises only JPEGs and PNGs.

### Contribute towards the expansion of the service:
As of now we have only one Machine Learning model that is capable of classifying the offensive content with an accuracy of ~92%. 
To expand the service for different medias like Gifs, Videos, all the other media that requires analysing the media frame by frame for classification :
1. We'll have to collect(scrap) the data from various websites like reddit(NSFW, SFW), instagram(NSFW, SFW), Twitter(NSFW, SFW) & Various pornography sites for 
   NSFW content.
2. Now that we have data, we need a Machine Learing Model. To build video classification models I recommend to give it a read. --> [Video Classification](https://www.analyticsvidhya.com/blog/2019/09/step-by-step-deep-learning-tutorial-video-classification-python/) & see this [YouTube](https://www.youtube.com/watch?v=SphaH33JU3Q) video to get an idea how to get started.
3. Build a Flask app with docker support for easy deployment.
4. Once the flask app is working, configure & add required settings in [Content Moderation App](https://github.com/RocketChat/Apps.Moderation) so that Rocket Chat
can send the video url to the flask app to send predictions to [Content Moderation App](https://github.com/RocketChat/Apps.Moderation) to take actions like blocking the media or not.

