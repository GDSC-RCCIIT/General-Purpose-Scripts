import json
import requests
import urllib.request
from os import path

dict = {
    1: {
        1: "pics",
        2: "PhotoshopBattles",
        3: "perfecttiming",
        4: "itookapicture",
        5: "Pareidolia",
        6: "ExpectationVSReality",
        7: "dogpictures",
        8: "misleadingthumbnails",
        9: "FifthWorldPics",
        10: "TheWayWeWere",
        11: "pic",
        12: "nocontextpics",
        13: "miniworlds",
        14: "foundpaper",
        15: "images",
        16: "screenshots",
    },
    2: {
        1: "mildlyinteresting",
        2: "interestingasfuck",
        3: "damnthatsinteresting",
        4: "beamazed",
        5: "reallifeshinies",
        6: "thatsinsane",
        7: "playitagainsam",
    },
    3: {
        1: "gentlemanboners",
        2: "prettygirls",
        3: "hardbodies",
        4: "girlsmirin",
        5: "thinspo",
        6: "goddesses",
        7: "shorthairedhotties",
        8: "fitandnatural",
        9: "wrestlewiththeplot",
        10: "skinnywithabs",
        11: "bois",
        12: "GentlemanBonersGifs",
    },
    4: {
        1: "asiancuties",
        2: "asiangirlsbeingcute",
    },
    5: {
        1: "PhotoshopBattles",
        2: "ColorizedHistory",
        3: "reallifedoodles",
        4: "HybridAnimals",
        5: "colorization",
    },
    6: {
        1: "amiugly",
        2: "roastme",
        3: "rateme",
        4: "uglyduckling",
        5: "prettygirlsuglyfaces",
    },
    7: {
        1: "wallpapers",
        2: "wallpaper",
        3: "Offensive_Wallpapers",
    },
}
SubReddit = ""
download_path = input("Enter the Path where you want to download Images.\n>> ")
if path.isdir(download_path) == False:
    print("Wrong Path Directory")
    quit()
if download_path[-1] != "/":
    download_path = download_path + "/"
num = input("Enter number of top Images you want to download (max:10) : \n>> ")
num = int(num)
if num > 10 or num < 1:
    print("Input should be >= 0 and <= 10")
    quit()
SearchType = input("Press : \n\t<1> For Custom Search\n\t<2> For Suggestion\n>> ")
if SearchType == "1":
    SubReddit_input = input("Enter SubReddit Name : ")
    if SubReddit_input.strip() == "":
        print("SubReddit can't be Null")
        quit()
    else:
        SubReddit_split = SubReddit_input.split("/")
        SubReddit = SubReddit_split[-1]
elif SearchType == "2":
    input1 = input(
        "Press : \n\t<1> For Category : Top\n\t<2> For Category : Interesting\n\t<3> For Category : Women\n\t<4> For Category : Asian\n\t<5> For Category : Photoshop\n\t<6> For Category : Selfies\n\t<7> For Category : Wallpapers\n>> "
    )
    int_input1 = int(input1)
    if int_input1 >= 1 and int_input1 <= 7:
        length = len(dict[int(input1)])
        print(length)
        print("Press : ")
        i = 0
        for i in range(1, length + 1):
            SubReddit_Suggestion = dict[int_input1][i]
            print("\t<" + str(i) + "> For SubReddit : " + str(SubReddit_Suggestion))
        input2 = input(">> ")
        int_input2 = int(input2)
        if int_input2 in range(1, i + 1):
            SubReddit = dict[int_input1][int_input2]
        else:
            print("Wrong Input")
            quit()
    else:
        print("Wrong Input")
        quit()
else:
    print("Wrong Input")
    quit()

result = requests.get(
    "https://www.reddit.com/r/" + str(SubReddit) + ".json?limit=" + str(10),
    headers={"User-agent": "Educational Purpose Scrapping"},
)
json_data = json.loads(result.text)

for j in range(0, num):
    try:
        title = json_data["data"]["children"][j]["data"]["title"]
        download_url = json_data["data"]["children"][j]["data"][
            "url_overridden_by_dest"
        ]
        extension = download_url[-4:]

        if extension == ".jpg" or extension == ".png":
            try:
                name = str(title) + str(extension)
                path_and_name = str(download_path) + str(name)
                urllib.request.urlretrieve(str(download_url), path_and_name)
                print(
                    str(j + 1)
                    + ") Name: "
                    + str(title)
                    + " || Type: "
                    + str(extension)
                    + " || URL: "
                    + str(download_url)
                    + "\n"
                )
            except:
                print("Unable to Download Image No. : " + str(j + 1))
                pass
    except:
        pass
