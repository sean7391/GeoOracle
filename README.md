# GeoOracle
Geolocation model for GeoGuessr. 

This respository contains the model code and sematic geocell algorithm code for my GeoGuessr AI. Image collection code as well as my datasets are not provided to prevent abuse and cheating with the bot. 

You can view the video demonstration here: https://youtu.be/Yt2UM2reNp4

The performance is comparable (if not better) to that of a professional GeoGuessr player. The dataset consists of mostly rural locations so it struggles on urban rounds.

I use the S2 cell library to recursively divide the world into 12,000+ cells based on density of images, discarding areas without coverage. This allows for extremely precise regionguessing. Currently, the model can accurately predict the correct cell over 33% of the time which is extremely impressive considering the number of cells and geographic size of cells. 

My model architecture uses InceptionResNetV2 for feature extraction, with a single output layer for grid classification. Finetuning is done using haversine distance as a metric, with an additional layer predicting coordinates using regression on top of the classification layer. 
