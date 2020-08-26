# NSFW Classifier
This project is started due to interactions between large communities among different channels in Rocket Chat, there was a need for support of an optional moderation service for offensive content (automated content moderation) for channels which can be deployed by an administrator on their sole discretion.

The Model basically classifies input image in 2 broad categories: 
1. NSFW(Not Safe for Work)
2. SFW(Safe for Work)

#  Data Collection And Organization
The data can be found below.

## For Images:

1. https://www.kaggle.com/omeret/nsfw-nsafe & https://www.kaggle.com/omeret/nsfw-safe.

2. [B Praneeth 's Data](https://archive.org/details/NudeNet_classifier_dataset_v1) .
   * Nude 
   * Sexy 
   *  Safe 
   
3. [Bazarov 's Dataset](https://github.com/EBazarov/nsfw_data_source_urls) . <br>
   * Female genitalia
   * Male genitalia 
   * Breasts <br>

4. [ Alex's Dataset](https://github.com/alex000kim/nsfw_data_scraper/tree/master/raw_data) . For classes **animated** and **porn** we can scrap the data from here.
  

5.  [Instagram Scrapper](https://github.com/rarcega/instagram-scraper) For class **Semi Nude** I used his tool to scrape few Instagram pages that regularly post arousing images of men and women.


6. https://archive.org/details/NudeNet_classifier_dataset_v1

7. https://github.com/alex000kim/nsfw_data_scraper

## For Videos:

1. [Resource 1](https://www.researchgate.net/publication/336430665_A_baseline_for_NSFW_video_detection_in_e-learning_environments)

2. [Dataset 2](https://www.kaggle.com/moradnejad/26-million-pornhub-videos-metadata-july-2019)

3. [Dataset 3](https://components.one/datasets/metadata-from-218000-pornhub-videos-jan-2008-dec-2018/)<br>
I also encourage everyone to read the piece this data was scraped for! [link](https://components.one/posts/every-story-is-an-epstein-story-stoya-pornhub-step-porn/)

4. The 2015 paper entitled ["Applying deep learning to classify pornographic images and videos"](https://arxiv.org/pdf/1511.08899.pdf) applied various types of convnets for detecting pornography. The proposed architecture achieved 94.1% accuracy on the NPDI dataset, which contains 800 videos (400 porn, 200 non-porn "easy" and 200 non-porn "difficult"). More traditional computer vision methods achieved 90.9% accuracy. The proposed architecture also performs very well regarding the ROC curve.<br> -Source: [StackExchange](https://ai.stackexchange.com/questions/1478/how-successfully-can-convnets-detect-nsfw-images)
