## Calculate Total Time Duration of YouTube Playlist

[![](https://img.shields.io/badge/Made_with-Python-red?style=for-the-badge&logo=python)](https://www.python.org/)
[![](https://img.shields.io/badge/Made_with-Google_Cloud%20api-blue?style=for-the-badge&logo=google-cloud)](https://console.cloud.google.com/)

### About
A Python script to calculte the Total Time Duration of any user inputted YouTube Playlist.

### Setup

* Install Python3 from [here](https://www.python.org/)
* Open Windows Command Prompt.
* Clone the repository
```bash
  git clone https://github.com/GDSC-RCCIIT/General-Purpose-Scripts.git
  ```
* Navigate inside the ```scripts/YouTube-Playlist-Duration``` directory.
* Run this command
```bash
  pip install -r requirements.txt
  ```
* Now go to [Google Cloud Console](https://console.cloud.google.com/).
* Then create a <b>New Project</b> from [here](https://console.cloud.google.com/projectcreate)
* Give an appropriate name to the Project and click <b>Create</b>.
* Then click on the <b>Navigation Menu</b> and then hover on <b>APIs & Services</b> and click on <b>Library</b>.
* There in the Search Bar, search for <b>
YouTube Data API v3</b> and click <b>Enable</b>
* Next click on <b>[Create Crendentials](https://console.cloud.google.com/apis/credentials)</b>.
* In the Credential Type, select YouTube Data API v3 and select Public Data and then click Done.
* Copy the API_KEY and paste it in the ```playlist_duration.py``` in the ```api_key``` variable at line 15.
* Now we are good to go. This was just a one time process.

Now copy the entire link of any playlist for which you want to find the time duration and paste it in the ```playlist_link``` variable in the ```playlist_duration.py``` at line 7.

Finally,
Run using Python:
```bash
  python playlist_duration.py
  ```
