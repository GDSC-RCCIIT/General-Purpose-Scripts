import requests
import json
import os
from logs.logger import logging as log


class Analyzer:
    BASE_URL = "https://sentim-api.herokuapp.com/api/v1/"

    def __init__(self):
        self.base_url = Analyzer.BASE_URL

    def read_textfile(self, args):
        with open(args) as f:
            lines = f.read().replace("\n", ".\n")
            return lines

    def get_sentiment(self, text):
        header = {"Accept": "application/json", "Content-Type": "application/json"}

        data = json.dumps({"text": text})

        response = requests.post(url=self.base_url, data=data, headers=header)
        if response.status_code == 200:
            response_text = json.loads(response.text)
            print(response_text)
            try:
                sentences = response_text["sentences"]
            except Exception as e:
                log.error("General Mood of the text: %s", "UNDEFINED"),

            if "result" in response_text.keys():
                polarity = response_text["result"]["polarity"]
                result_type = response_text["result"]["type"]

                log.info("General Mood of the text: %s", result_type.upper()),
                log.info("Percentage of Polarity: %i percent", (round(polarity * 100))),
                log.info("Number of sentences evaluated: %s", len(sentences))

            if "sentences" in response_text.keys():
                positive_ctr, negative_ctr, neutral_ctr = 0, 0, 0
                for sentence in sentences:
                    if sentence["sentiment"]["type"] == "positive":
                        positive_ctr += 1
                    elif sentence["sentiment"]["type"] == "negative":
                        negative_ctr += 1
                    else:
                        neutral_ctr += 1

            log.info("Positive sentences: %s", positive_ctr)
            log.info("Negative sentences: %s", negative_ctr)
            log.info("Neutral sentences: %s", neutral_ctr)

        else:
            log.error("General Mood of the text: %s", "UNDEFINED")

    def main(self):
        text = self.read_textfile("analyze_file.txt")
        bot.get_sentiment(text)


if __name__ == "__main__":
    bot = Analyzer()
    bot.main()
