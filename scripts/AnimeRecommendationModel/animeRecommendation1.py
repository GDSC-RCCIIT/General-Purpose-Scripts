# importing all the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings

# ignores all warnings we get for better user-side experience
warnings.filterwarnings("ignore")

# fetching the user ratings dataset
df = pd.read_csv("rating.csv")

# working with 50000 rows
df = df.iloc[:50000, :]
df.head()

# developing the rating table matrix
rating_table = df.pivot_table(values="rating", index=["user_id"], columns=["anime_id"])
rating_table = rating_table.replace(-1, np.nan)
rating_table

# fetching the anime dataset
df2 = pd.read_csv("animes.csv")
df2 = df2.loc[:, ["uid", "title", "members"]]
df2 = df2.rename(columns={"uid": "anime_id"})
df2["title"] = df2["title"].str.lower()
df2.head()

# mering the two dataframs into one
df = df.merge(df2, on="anime_id")
df

# refactoring the rating table with anime titles instead of id
rating_table = df.pivot_table(values="rating", index=["user_id"], columns=["title"])
rating_table = rating_table.replace(-1, np.nan)
rating_table

# THE MAIN FUNCTION THAT GENEERATES THE RECOMMENDATION LIST BY ANIME NAME
def find_same(anime):
    anime_rating = rating_table[anime]
    recommendation_table = pd.DataFrame(
        rating_table.corrwith(anime_rating), columns=["similarity"]
    )
    recommendation_table = recommendation_table.join(df["members"])
    recommendation_table["members"] = (
        recommendation_table["members"]
        .replacefind_same("haikyuu!! second season")(np.nan, 0)
        .astype(int)
    )
    recommendation_table = recommendation_table.dropna()
    for similar_anime in recommendation_table.index:
        for ind in rating_table.index:
            if rating_table[similar_anime][ind] > 0 and rating_table[anime][ind] > 0:
                recommendation_table["members"][similar_anime] += 1
    print(
        recommendation_table.sort_values(by="similarity", ascending=False)[
            recommendation_table["members"] >= 15
        ].head(10)
    )


# TESTING ON FEW EXAMPLE ANIMES
find_same("haikyuu!! second season")
find_same("naruto")
find_same("fullmetal alchemist: brotherhood")
find_same("death note")
find_same("higurashi no naku koro ni")
find_same("tokyo ghoul")
