# importing all the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings

# ignores all warnings we get for better user-side experience
warnings.filterwarnings("ignore")

# fetching the required columns from anime dataset
df = (
    pd.read_csv("animes.csv")
    .loc[:, ["uid", "title", "members", "synopsis"]]
    .rename(columns={"uid": "anime_id"})
)
df["title"] = df["title"].str.lower()
df

# cleaning the dataset
df["synopsis"] = df["synopsis"].str.replace("\r", "")
df["synopsis"] = df["synopsis"].str.replace("\n", "")
df["synopsis"] = df["synopsis"].fillna("")

for i in range(0, 19311):
    df["synopsis"][i] = df["synopsis"][i].split("  [")[0]


# saving the cleaned dataset
df.to_csv("anime_dataset.csv")

# fetching the cleaned dataset
df = pd.read_csv("anime_dataset.csv").iloc[:5000, 1:]
df = df.sort_values(by="anime_id").drop_duplicates(subset=["title"])

# importing the Count Vectorisation class and making a vectoriser object
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=5000, stop_words="english")

# making the text vectoriser bag of words
tv = cv.fit_transform(df["synopsis"].astype("U")).toarray()

# now importing cosine similarity from sklearn and applying it on the bag of words
from sklearn.metrics.pairwise import cosine_similarity

cos_sim = cosine_similarity(tv)
cos_sim

# THE MAIN FUNCTION WHICH RECOMMENDS 10 ANIMES CLOSEST TO THE GIVEN ANIME BASED ON THE SYNOPSIS
def recommender(anime):
    index = df[df["title"] == anime].index[0]
    distances = sorted(
        list(enumerate(cos_sim[index])), reverse=True, key=lambda x: x[1]
    )
    for i in distances[1:10]:
        print(df.iloc[i[0]].title)


# FEW TEST RUNS
recommender("made in abyss")
recommender("dragon ball")
recommender("death note")
recommender("one piece")
