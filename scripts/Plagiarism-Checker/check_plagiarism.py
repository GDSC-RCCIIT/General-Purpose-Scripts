from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

data = pd.read_csv("data.csv")


def check_plagiarism(data):
    similarity_list = []

    for i in range(len(data)):
        corpus = [data["text1"][i], data["text2"][i]]
        vectors = TfidfVectorizer().fit_transform(corpus).toarray()

        text1_vector = [vectors[0]]
        text2_vector = [vectors[1]]

        similarity = cosine_similarity(text1_vector, text2_vector)[0][0]
        similarity_list.append(similarity)

    return similarity_list


similarity_list = check_plagiarism(data)
data["similarity"] = similarity_list

data.to_csv("output.csv", index=False)
