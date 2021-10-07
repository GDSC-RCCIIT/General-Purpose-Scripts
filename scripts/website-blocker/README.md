# Website Blocker
This is real world program which blocks certain distracting website like Facebook, Youtube etc during your work hours.

What we are going to in this program is that we will pass the link of websites which you think is distracting and the time that you are working on your computer and program will block those website.

  

### Working of host file:
Host is an operating system file which maps hostnames to IP addresses. In this program we will be mapping hostnames of websites to our localhost address. Using python file handling manipulation we will write the hostname in hosts.txt and remove the lines after your working hours.

  

**Special note for Windows users** :*Windows user need to create a duplicate of OS’s host file. Now provide the path of the duplicate file in hosts_path mentioned in the script.*

Things to remember :-
* Run this program as root
* This is not a scheduled after you restart your computer
* Windows users must create a duplicate of your hosts file

### How to add Websites to block :-
Add the websites to block in the `websites.csv` file.

### Running the file :-
*For MacOS and Linux:*

    sudo su
    python3 main.py
*For Windows:*

Open a CMD with administrative privileges, then

    python3 main.py
