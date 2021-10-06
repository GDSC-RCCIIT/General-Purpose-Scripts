## LinkedIn Job Scraper

![python](https://img.shields.io/badge/language-Python-orange?style=for-the-badge)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=plasitc)](https://github.com/psf/black)

### About

A Python3 script to <b>scrap</b> best job fitted for you from [`LinkedIn`](https://www.linkedin.com/jobs/) according to the given input <br>and saves them in `.csv` file named `linkedin-job-scrapper.csv`

Note : Header of `.csv` file will look like this :

| id  | Job | Company | Details | Location | Upload Date | Link |
| --- | --- | ------- | ------- | -------- | ----------- | ---- |
|     |     |         |         |          |             |

### User Manual

You can search Jobs by 2 methods :

1. `Direct Search` (Using your IP Address)*
2. `Custom Search` (Recommended)*

If you have entered `2` previously then :

1. Enter : Your `City` \*
2. Enter : Your `Job Profile` \*
3. Enter :
   - `1` : To Enter Types of Job you want. (eg. Internship , Entry Level)
   - `2` : To Enter Job Type : Full-Time or Part-Time
   - `0` : To `esc` this step *

### Setup

To install the required libraries :
<br><b>Run:</b>

```
pip install -r requirements.txt
```

### Screenshots

<details><summary><b>Direct Search : </b></summary>
<img width="1440" alt="Direct Search" src="https://user-images.githubusercontent.com/82683890/136022659-448923a3-65b5-4ac6-96e7-f0bc2f241d2a.png">
</details>
<details><summary><b>Custom Search :</b></summary>
<img width="1440" alt="Custom Search" src="https://user-images.githubusercontent.com/82683890/136022637-f4feb648-674a-418c-b88f-030172d93d6e.png">
</details>

### Video

https://user-images.githubusercontent.com/82683890/136023434-66482197-1232-47f6-85ec-90ef45d7140c.mp4
