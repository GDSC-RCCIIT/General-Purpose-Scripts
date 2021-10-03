## Scrape Tweets of a Hashtag using Twitter API

[![](https://img.shields.io/badge/Made_with-Python-red?style=for-the-badge&logo=flutter)](https://www.python.org/)
[![](https://img.shields.io/badge/Made_with-twitter%20api-blue?style=for-the-badge&logo=twitter)](https://developer.twitter.com/en/portal/products)

### About
A Python script to scrape the most recent 100 tweets of any user inputted Hashtag and creates a csv file of the same

### Setup

* Install Python3 from [here](https://www.python.org/)
* Open Windows Command Prompt.
* Clone the repository
```bash
  git clone https://github.com/GDSC-RCCIIT/General-Purpose-Scripts.git
  ```
* Navigate inside the ```scripts/Twitter-Scraper``` directory.
* Run this command
```bash
  pip install -r requirements.txt
  ```
* Firstly create a Twitter account if you don't have one.
* Then go to the [Developer Platform of Twitter](https://developer.twitter.com)
* Apply for a Developer account by clicking <b>Apply</b>
* Fill the Application Form. It is a very straightforward and easy procedure.
* After you fill this Application, you will receive a mail regarding acceptance of your request within 1-2 days.
* Then go to [Projects and Apps](https://developer.twitter.com/en/portal/projects-and-apps) page in the Developer Portal.
* There click on <b>New Project</b> and fill all the details about the project (name, description etc.)
* Now copy the API Key and the API Secret Key and paste in the ```twitter_credentials.py``` file in the respective fields.
* Then go to App Settings and click on Generate Access Token and Secret and copy them and paste in the ```twitter_credentials.py``` file in the respective fields.
* Now we are good to go.

Run using Python:
```bash
  python tweet_scraper.py
  ```
* Now you have to type the <b>Hashtag</b> for which you want to scrape the Tweets (for example: #Messi, #India, etc.)
* You will get the output in the <b>"outputs"</b> folder in the same directory as a <b>CSV File</b>

