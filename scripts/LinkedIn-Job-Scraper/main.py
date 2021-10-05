import requests
import geocoder
from bs4 import BeautifulSoup
import csv

header = ["Id", "Job", "Company", "Details", "Location", "Upload Date", "Link"]
filename = "linkedin-job-scraper.csv"

url = "https://www.linkedin.com/jobs/search?"
location = "location="
profile = "&keywords="
position = "&f_E="
jobtype = "&f_JT="
sort = "&sortBy="
search_type = input(
    "Enter : \n\t<1> For Direct Search\n\t<2> For Custom Search (Recommended)\n>> "
)

if search_type == "1":
    loc = geocoder.ipinfo("me")
    state_input = str(loc.state)
    state_input = state_input.replace(" ", "%20").lower()
    location = location + str(state_input)
    url = url + location
elif search_type == "2":
    city_input = input("Please Enter Your City : \n>> ")
    city_input = city_input.replace(" ", "").lower()
    location = location + str(city_input)
    url = url + location
    job_input = input("Please Enter Your Job Profile : \n>> ")
    job_input = job_input.replace(" ", "").lower()
    profile = profile + str(job_input)
    url = url + profile
    types_input = ""
    bool_pre_position = False
    bool_pre_type = False
    while types_input != "0":
        print("Enter : ")
        if bool_pre_position == False:
            print("\t<1> For : Job Position")
        if bool_pre_type == False:
            print("\t<2> For : Job Type")
        types_input = input("\t<0> To esc\n>> ")
        if types_input == "1":
            bool_pre_position = True
            bool_positional = False
            while bool_positional == False:
                position_input = input(
                    "Enter : \n\t<1> For : Internship\n\t<2> For : Entry Level\n\t<3> For : Associate\n\t<4> For : Mid Senior Level\n\t<5> For : Director\n\t<6> For : Executive\n >> "
                )
                if position_input == "1":
                    bool_positional = True
                    position = position + str("1")
                elif position_input == "2":
                    bool_positional = True
                    position = position + str("2")
                elif position_input == "3":
                    bool_positional = True
                    position = position + str("3")
                elif position_input == "4":
                    bool_positional = True
                    position = position + str("4")
                elif position_input == "5":
                    bool_positional = True
                    position = position + str("5")
                else:
                    continue
            url = url + position
        elif types_input == "2":
            bool_pre_type = True
            bool_jobtype = False
            while bool_jobtype == False:
                jobtype_input = input(
                    "Enter : \n\t<1> For : Full Time Job\n\t<2> For : Part Time Job\n>> "
                )
                if jobtype_input == "1":
                    bool_jobtype = True
                    jobtype = jobtype + str("F")
                elif jobtype_input == "2":
                    bool_jobtype = True
                    jobtype = jobtype + str("P")
                else:
                    continue
            url = url + jobtype

        if bool_pre_position == True and bool_pre_type == True:
            break
else:
    print("Wrong Input")
    quit()


try:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    body = soup.find("body")
    with open("linkedin-job-scraper.csv", "a", newline="") as f:
        writer = csv.writer(f)
        i = 0
        for content in body.findAll("div", {"class": "base-search-card__info"}):
            try:
                Title = str(
                    content.find("h3", {"class": "base-search-card__title"}).getText()
                )
                Title = " ".join(Title.split())
                Company = str(
                    content.find("a", {"class": "hidden-nested-link"}).get_text()
                )
                Company = " ".join(Company.split())
                Link = str(
                    content.find("a", {"class": "hidden-nested-link"}).get("href")
                )
                Link = " ".join(Link.split())
                Location = str(
                    content.find(
                        "span", {"class": "job-search-card__location"}
                    ).get_text()
                )
                Location = " ".join(Location.split())
                Details = str(
                    content.find("p", {"class": "job-search-card__snippet"}).get_text()
                )
                Details = " ".join(Details.split())
                Time = str(
                    content.find(
                        "time", {"class": "job-search-card__listdate"}
                    ).get_text()
                )
                Time = " ".join(Time.split())
                print("Title : " + str(" ".join(Title.split())))
                print("Company : " + str(" ".join(Company.split())))
                print("Details : " + str(" ".join(Details.split())))
                print("Location : " + str(" ".join(Location.split())))
                print("Time : " + str(" ".join(Time.split())))
                print("Link : " + str(" ".join(Link.split())))
                print("\n")
                i = i + 1
                writer.writerow([i, Title, Company, Details, Location, Time, Link])
            except:
                pass
        f.close()
except requests.HTTPError as err:
    print("Unable to Scrap !!")
