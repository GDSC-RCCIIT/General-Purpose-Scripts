import requests

URI = "https://api.dictionaryapi.dev/api/v2/entries/en/"


def main():
    word = input("Enter the word to Search Meaning : ")
    URI_ = URI + word
    reqs = requests.get(URI_).json()
    try:
        return print(reqs["title"])
    except (KeyError, TypeError):
        pass
    dfn = reqs[0]["meanings"][0]["definitions"][0]
    text = f"\n• Word : {word}"
    text += f"\n• Definition : {dfn['definition']}"
    text += f"\n\n• Example : {dfn['example']}"
    print(text)


main()
