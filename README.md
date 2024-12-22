# General Purpose Scripts

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=plasitc)](https://github.com/psf/black)
![License](https://img.shields.io/github/license/GDSC-RCCIIT/General-Purpose-Scripts?color=blue&style=plasitc)
![Contributors](https://img.shields.io/github/contributors/GDSC-RCCIIT/General-Purpose-Scripts?color=darkgreen&style=plasitc)
![Forks](https://img.shields.io/github/forks/GDSC-RCCIIT/General-Purpose-Scripts?color=purple&style=plasitc)

## Introduction

This repository holds a curated list of Python scripts which aim to help us automate daily and common tasks. You can pick up any of these scripts on demand to help you with the automation of your common routine tasks. All the scripts in this repository can be found under the `scripts` directory and have been contributed by our generous contributors.

## Install any script using gpscript command

First of all install gpscript. Write following command(s)
```
pip install gpscript
```
or,
```
git clone https://github.com/ujjwalkar0/gpscript

cd gpscript

python setup.py install

```
List of all script (Only those packages are in packages.json will shown here.)

```
gpscript list
```
Install a script
```
gpscript install <package_name>
```

List all installed packages...
```
gpscript installed
```
Remove a package...
```
gpscript remove <package_name>
```
Update a package...
```
gpscript update <package_name>
```

## Developer Guidelines
Path of installation script is `<path_of_virtualenv>/applications/<your_script_folder>`. applications folder will create automatically in virtualenv when a script will install

Before installation any script..

![image](https://user-images.githubusercontent.com/55041104/140525324-19765c22-a75f-4777-a618-d0cbf55b8e68.png)


Let we Install `LinkedIn-Job-Scraper`

![image](https://user-images.githubusercontent.com/55041104/140558125-d96e36b8-192d-468f-ae99-6133fcc214c4.png)
 

![image](https://user-images.githubusercontent.com/55041104/140558534-cd1715ba-01f3-41fc-ae08-8ee1a2e34742.png)

So, set the path uses location that way...

```python
import os
base_dir = os.path.dirname(os.path.realpath(__file__))
```

Set path of script relative to base_dir

For example,

![image](https://user-images.githubusercontent.com/55041104/140559355-7dc8bc41-8316-4223-a78d-6804f439850f.png)

![image](https://user-images.githubusercontent.com/55041104/140559465-42a80f03-196a-47dd-b121-870670f91f2c.png)


## How to contribute

Our repository accepts all kinds of contributions. Before making a contribution please make sure you have gone through our [contributing guidelines](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/blob/main/.github/CONTRIBUTING.md).

You can open an issue with us for a bug, feature or a new script or start working on an existing issue after having it assigned to you by one of the maintainers.

## Things to keep in mind when contributing


If you are adding a script to the respository, please create a separate directory with the name of the script inside the `scripts` directory of this repository and work within it. Make sure your script comes with its very own `README.md` with proper documentation for the end user, if possible add screenshots of your script working in the `README.md` as well. In case you are uploading screenshots and/or other relevant images please create a separate `images` folder inside your script folder, this is where you will be keeping your images. Alternatively, you can also upload your images on platforms like [imgur](https://imgur.com/) and use the resulting link in your `README.md` file.


Once you are done working on your script edit this `README.md` file and add the relevant information regarding your script in the table below.

## Available Scripts in our Repository

| Id No. | Script Name               | Script Description                                                           | Link                                                                                                       |
| ------------ | ------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
1| Amazon-Price-Alert        | Send a Email to the user when the price of product goes down below threshold | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/amazon-price-alert) |
2| AudioBook                 | Converts PDF-to-speech                                                       | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/AudioBook)            |
3| Automatic Screen Recorder | script to record the laptop screen automatically                             | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Automatic%20screen%20recorder)                             |
4|Ceaser Cipher | script to encode and decode | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Ceaser%20Cipher)
5|Covid Tracker | script which tracks the number of cases, deaths and recovered cases of covid patients| [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Covid-Tracker)
6| CP Template Maker | Organizes and creates templates for cp contests | [Find me Here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/CpTemplate) 
7| Check-System-Usage | Checks free space percentage and average CPU usage | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Check-System-Usage) |
8| Command line chart tool | script to make fast pie charts from command line | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/pie_chart_maker) |
9| CryptoCurrency | Fetches cryptocurrency data and stores them in a .csv file | [Find me Here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/CryptoCurrency) |
10| Currency Converter | Convert currencies on realtime using a beautiful tkinter GUI | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Currency-Converter) |
11| Doc to PDF Converter | Converts docx file(s) to PDF files | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Docx%20To%20PDF%20Converter) |
12| Email Sender | Automates Email Process | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Email-Sender) |
13| Email-Phone-Extractor | Extracts email addresses and phone number from clipboard or a text file and stores them as separate csvs | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/email_phone_extractor) |
14| File Organizer | Organize your Files | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/File%20Organizer) |
15| Handwriting Recognition Module | Detects hand and returns coordinate of various points on hand in a live stream | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/HandDetectionModule)
16| Image Compressor | Script compress Images | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/image-compressor) |
17| JSON to xlsx converter | Script to convert json to xlsx | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Json-xlsx) |
18| LinkedIn Job Scraper | Scrap Jobs listed in LinkedIn & saves them in `.csv` file | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/LinkedIn-Job-Scraper) |
19| Meaning Finder | Find Word's Meaning.. | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Meaning%20Finder) |
20| News Reader Script | Script to read news | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/NewsReader) |
21| NewsDown | It can download the newspaper in one click | [Find me Here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/NewsDown) |
22| Notice Scrapper | Extract all notices from rcciit.org | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/NoticeScrapper) |
23| OCR Script Scanner | Extracts text from image file by scanning it | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/OCR_Scanner) |
24| OSINT Tool | Help Find OSINT info about phone number & IP address | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/OSINT_TOOLS) |
25| PDF_Merger_Script | Script to merge pdf | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/pdf_merger)
26| Password Leak Checker | How many times your password has been breached | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/PasswordStrengthChecker)
27| Public IP Address | Prints your public IP address | [Find me Here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Public%20IP%20Address) |
28| QR Code Generator | It can generate QR Code of URLs | [Find me Here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/QR%20Code%20Generator) |
29| Reddit Image Scrapper | Downloads Reddit Images according to given SubReddit without using API | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Reddit-Image-Scrapper) |
30| SMS Sender | Easy CLI interface for users looking to test their SMS campaign integration with Kaleyra | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/SMS%20Sender) |
31| Shorty | Shorty uses python code to shorten URLs on the go | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Shorty) |
32| Image to Sketch Converter | Script which converts a colored photo into pencil sketch or cartoonized sketch | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/image_to_sketch_converter) |
33| Song-Lyrics-Fetcher | Fetch lyrics of a song and store in a text file | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Song-Lyrics-Fetcher) |
34| Spectrogram | script to visualize wav files using spectrogram | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/spectrogram) |
35| Terminal Video Editor | Edit Small Videos (less than : 10 mins) directly from your Terminal | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Terminal-Video-Editor) |
36| Text Grammar Corrector | Corrects Grammar of text | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Text%20Grammar%20Corrector)
37| Twitter-Scraper | Scrape Tweets of a user-inputted Hashtag | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Twitter-Scraper) |
38| Vaccination Centre Locator | Provides top 10 nearest Vaccination Centres data based on location in India | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Vaccination-Centre-Locator) |
39| Weather_Forecast_Script | Script to forecast weather of a city | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/weather_forecast) |
40| Word Cloud Generator | Converts text entered into a Word Cloud | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Word-Cloud-Generator) |
41| Yaml-Json-Generator | Generate JSON files from YAML files in a directory | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Yaml-Json-Generator) |
42| Youtube-Playlist-Duration | Calculates the total duration of a Youtube Playlist | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Youtube-Playlist-Duration) |
43| QR_SCANNER | script which Decode QR code | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/QR_CODE_SCANNER) |
44| VideoCam | Takes pictures and records vidoes using your webcam | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/VideoCam) |
45| Notification Reminder | Script to create popup notification | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Notification_Reminder)
46| Website Blocker | Cross-Platform website blocker | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/website-blocker)
47| Anime Recommendation Model| Recommed 10 animes to watch next based on an anime you loved | [Find me here](https://github.com/Anubhab2002/General-Purpose-Scripts/tree/main/scripts/AnimeRecommendationModel) |
48| AI Workout Tracker | AI based workout tracker that is able to detect body landmarks and present you the results | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/AI%20Workout%20Tracker)
49| Volume Control OpenCV | Simple GUI for users to control volume of control systems with their hands via handtracking | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/volume_control_opencv)
50| Password Manager | AES encrypted password manager to keep all your password safe | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Password_Manager) |
51| Battery Alert    | Notifies after threshold unit of battery change | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Battery-Notifier) |
52| Text To Handwriting Converter    | Converts a text or a text file to handwritten images | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/text_to_handwriting_converter) |
53| Typing Speed Tester    | Calculates the typing speed of users. | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/typing_speed_test) |
54| Video To GIF Converter    | Converts video to GIF | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Video_to_GIF_Converter) |
55| Auto Backup       | Backups the folder given by the user in the input. | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Auto-Backup) |
56| Metadata Extractor    | Extracts Meta Data of Image | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/image-metadata)|
57| alarm-clock      | Console based Alarm clock and remainder which plays sound and shows message as user directed | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/alarm-clock) |
58| CryptoCurrencyTracker | Gets the values of the cryptocurrency data from the given url and stores updates them in a .csv file continiously for every 10 minutes | [Find me Here](https://github.com/Tanuj2552/General-Purpose-Scripts/tree/main/scripts/CryptoCurrencyTracker) |
59| Voice-to-text Converter | Transcribes speech from inputted audio file using PocketSphinx. | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/voice_to_text) |
60| Steganography | Text Encryption and Decryption to and from an Image | [Find me Here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/steganography) |
61| Instagram Photo Downloader    | Downloads photos from Instagram. | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Instagram%20Photo%20Downloader) |
62| PDF2text | Extracts text from a pdf file and display it to the user. | [Find me Here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/PDF2text/) |
63| Image to PDF converter| Converts all the images which is inside a dir to a PDF file | [Find me Here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/image_to_pdf) |
64| PDF to Docx Converter    | Converts PDF file to Docx | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/PDF%20to%20Docx%20Converter) |
65| Threaded Port Scanner    | Tool for scanning open ports on a host | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Threaded-Port-Scanner) |
66| Z-test Calculator    | Calculates Z-statistic Value for the given set of Numerical Data and Population Mean | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/zcal/scripts/Z-test%20Calculator) |
67| Music Visualizer    | Creates a visualization of any music file | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/janinirami/scripts/Music-Visualizer) |
68| Mood Sentiment Analyzer| Evaluate given texts/sentences general mood. | [Find me Here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Mood%20Sentiment%20Analyzer)
69| Morse Code Translation    | Convert morse code to english language and vice versa | [Find me here](https://github.com/mahalrupi/General-Purpose-Scripts/tree/main/scripts/Morse-code-translation)
70| Plagiarism Checker| Find similarity/plagiarism score between 2 texts | [Find me Here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Plagiarism-Checker)
71| Water Reminder | Reminds you to drink water every 2 hours | [Find me Here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Water%20Reminder)
72| QR and Barcode Scanner | Scans both QR Codes and Barcodes | [Find me Here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/QR%20and%20Barcode%20Scanner)   |
73| PDF-Delete-Pages | Deletes pages from PDF as entered by the user | [Find me Here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/PDF-Delete-Pages)   |
74| Copy to clipboard | Copies contents form a text file to your clipboard | [Find me Here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Copy%20to%20clipboard)   |
75| Video-to-audio Convertor    | Extracts audios from videos. | [Find me here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Video-to-audio-convertor) |
76| Audio Recorder | Records audio from system's audio input device for `n` seconds | [Find me Here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/Audio%20Recorder)   |
77| NATO Phonetic Alphabet | Spells entered word using NATO phonetic alphabets | [Find me Here](https://github.com/GDSC-RCCIIT/General-Purpose-Scripts/tree/main/scripts/NATO%20Alphabet)   |
### Good Luck and don't forget to have fun with Open Source General-Purpose-Scripts💻🚀