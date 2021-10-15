## Introduction
Hello interested people, this directory contains implementions based on **Machine Learning Algorithms** for **recommending animes** similar to an anime that you have recently watched and fed into the models. 

## Descriptoon
There are 2 python scripts for 2 different logic implementation in this directory ( ``animeRecommendation1`` and ``animeRecommendation2``) where:
- The first model is based on Correlation between anime where the most correlated anime are suggested to you. Infact this model is pretty accurate and has an accuracy of around 70%-80% with a dataset of only 4400 animes. This is based on similar user ratings and watching habits.
- The second model is based on the concept of Text Vectorisation implemented with Bag of Word (BoW) method. Then the cosine similarity with all other animes are found and the 10 nearest vectors(similar anime) are given to you. As od now this model is very basic and a bit inaccurate and there is scope of improvement. This model is based on similarity in the synopsis of two animes.

**NOTE**: On one hand, the 1st model is very accurate with the results it provides while on the other hand, the 2nd model is very fast but a bit inaccurate.

## Before you start
1. Download ```rating.csv``` from [Kaggle](https://www.kaggle.com/CooperUnion/anime-recommendations-database?select=rating.csv) and put it in your working directory. Its too large to add to the repository. The other required datasets have been provided in the directory itself.
2. Install all the required libraries and dependencies using the command ```pip install -r requirements.txt``` in the terminal inside this directory.


### Visit my [Github Profile](https://github.com/Anubhab2002) for more interesting projects and do't forget to follow me!
