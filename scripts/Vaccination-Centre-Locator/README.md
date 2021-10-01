## Vaccination Cerntre Locator based in India

![python](https://img.shields.io/badge/language-Python-orange?style=for-the-badge)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=plasitc)](https://github.com/psf/black)

### About

A Python3 script to provide top 10 nearest Vaccination Centre to you.
<br>You can search Vaccination Centres using :
1) <b>Zip Code</b>
2) <b>Network Data (Mac Address)</b>
3) <b>Location Data</b>
4) <b>IP Address</b>

If you search Vaccination Centre using `Zip Code` (Recommended) <br>then you will get complete details like: 
1) <b>Centre Name</b>
2) <b>Address</b>
3) <b>Time Slots</b>
4) <b>Vaccine Name</b>
5) <b>Price</b>
6) <b>Avaibility (Dose 1 + Dose 2)</b>

In other 3 cases you will get only 
1) <b>Centre Name</b>
2) <b>Address</b>

### Setup

To search Vaccination Centre using `Network Data (Mac Address)` you need to have API Key (<b>Google's Geolocation API</b>).

To get such follow these steps:

* Go to the [Google Maps Platform](https://cloud.google.com/maps-platform)
* Click the `Get Started` button.
* Click on the `Hamburger Icon (☰)` upper left corner.
* Click on `Billing` to make sure your billing details are up-to-date. If they not, follow this [link](https://swapps.com/blog/setting-up-your-billing-account-on-google-maps-and-avoiding-extra-charges/).
* Once you’ve confirmed your billing is up-to-date, click on the `Hamburger Icon (☰)` upper left corner again.
* If you want to use an existing project, please select it from the dropdown menu beside `Google Cloud Platform`. Otherwise, follow same & select `New Project` and enter a project name and link that with the new billing id.
* Click on the `Hamburger Icon (☰)` upper left corner again.
* Hover to `APIs & Services` and go to `Library`.
* Search `Geolocation API` and `enable` it.
* Click on the `Hamburger Icon (☰)` upper left corner again.
* Hover to `APIs & Services` and go to `Credentials`.
* Click `Create credentials` and select `API key`. You will see a new dialog that displays the newly created `API key` and copy that.
* Now in `main.py` file paste that API Key inside the string on `line no. 9`.

### Screenshots
<details><summary>1) Search using <b>Zipcode</b></summary>
<img width="650" alt="1" src="https://user-images.githubusercontent.com/82683890/135646191-893aa3f7-a942-475f-bca9-c743c332ba0e.png">
</details>

<details><summary>2) Search using <b>Network Data (Mac Address)</b></summary>
<img width="650" alt="2" src="https://user-images.githubusercontent.com/82683890/135646209-a3b5fdf8-5357-4d69-884e-02ebc6f6e6e2.png">
</details>

<details><summary>3) Search using <b>Location Data</b></summary>
<img width="600" alt="3" src="https://user-images.githubusercontent.com/82683890/135646213-9e9b71fd-6f50-4d7b-aebd-97ad6df1fccf.png">
</details>

<details><summary>4) Search using <b>IP Address</b></summary>
<img width="650" alt="4" src="https://user-images.githubusercontent.com/82683890/135646218-4cb2a472-1650-4bac-8b9d-5b2ed47fe456.png">
</details>


