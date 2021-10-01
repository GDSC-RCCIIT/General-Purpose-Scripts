import random
import base64
import pickle


def AutoGen():
    passwd = ""
    for i in range(12):
        passwd += chr(random.randint(33, 126))
    return passwd


def Add_Passwd(site, user, passwd):
    file = open("scripts/Password_Manager/data.dat", "ab")
    enc_passwd = base64.b64encode(passwd.encode("utf-8"))
    enc_user = base64.b64encode(user.encode("utf-8"))
    enc_site = base64.b64encode(site.encode("utf-8"))
    E1 = {"site": enc_site, "user": enc_user, "passwd": enc_passwd}
    pickle.dump(E1, file)


def Print_Passwd(site):
    file = open("scripts/Password_Manager/data.dat", "rb")
    try:
        while True:
            x = pickle.load(file)
            z = (
                str(base64.b64decode(x["site"].decode("utf-8")))
                .lstrip("b'")
                .rstrip("'")
            )
            if site == z:
                user = (
                    str(base64.b64decode(x["user"].decode("utf-8")))
                    .lstrip("b'")
                    .rstrip("'")
                )
                passwd = (
                    str(base64.b64decode(x["passwd"].decode("utf-8")))
                    .lstrip("b'")
                    .rstrip("'")
                )
                return user, passwd
    except:
        pass


while True:
    x = """1. Generate random password
    2. Save password
    3. Search
    to quit type `exit` """
    print(x)
    command = input(">>")
    if command == "1":
        print(AutoGen())
    elif command == "2":
        print("enter site, user & password seperated by space ")
        data = list(input("here: ").split(" "))
        Add_Passwd(data[0], data[1], data[2])
    elif command == "3":
        data = input("Enter site name: ")
        user, passwd = Print_Passwd(data)
        print(user, "|", passwd)
    elif command == "exit":
        break
    else:
        print("No such command exist")
