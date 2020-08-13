# NSFW Classifier
This project is started due to interactions between large communities among different channels in Rocket Chat, there was a need for support of an optional moderation service for offensive content (automated content moderation) for channels which can be deployed by an administrator on their sole discretion.

The Model basically classifies input image in 2 broad categories: 
1. NSFW(Not Safe for Work)
2. SFW(Safe for Work)

#  Data Collection And Organization
The data can be found below.

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