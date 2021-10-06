import random
import base64
import pickle
from Crypto.Cipher import AES
import hashlib
import os


def checkForFile():
    path = "master.dat"
    isExist = os.path.exists(path)
    return isExist


def master_Encrypt(master):
    passwd = bytes(master, "utf-8")
    result = hashlib.md5(passwd)
    pasit = result.digest()
    return pasit


def store_master(master):
    file = open("master.dat", "wb")
    crp_pass = master_Encrypt(master)
    file.write(crp_pass)


def read_master():
    file = open("master.dat", "rb")
    data = file.read()
    return data


def AutoGen(number):
    passwd = ""
    for i in range(number):
        passwd += chr(random.randint(33, 126))
    return passwd


def encrypt_file(message):

    key = read_master()

    mode = AES.MODE_CBC

    IV = "This is an IV456"

    cipher = AES.new(key, mode, IV)

    encrypt_message = cipher.encrypt(message)
    return encrypt_message


def decrypt_file(code):

    key = read_master()
    mode = AES.MODE_CBC
    IV = "This is an IV456"
    cipher = AES.new(key, mode, IV)

    decrypt_message = str(cipher.decrypt(code)).lstrip("b'").rstrip("'")
    return decrypt_message


def Add_Passwd(site, user, passwd):
    file = open("data.dat", "ab")
    enc_passwd = encrypt_file(passwd)
    enc_user = base64.b64encode(user.encode("utf-8"))
    enc_site = base64.b64encode(site.encode("utf-8"))
    E1 = {"site": enc_site, "user": enc_user, "passwd": enc_passwd}
    pickle.dump(E1, file)


def Print_Passwd(site):
    file = open("data.dat", "rb")
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
                passwd = decrypt_file(x["passwd"])
                return user, passwd
    except:
        pass


def main():
    while True:
        x = """
        1. Generate random password
        2. Save password
        3. Search
        to quit type `exit` """
        print(x)
        command = input(">>")

        if command == "1":
            user = int(input("Enter size of password (recommended 12) >>"))
            print(AutoGen(user))

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


if checkForFile() == True:
    passCheck = input("Enter master key = ")
    key_enc = read_master()
    if key_enc == master_Encrypt(passCheck):
        main()
    else:
        print("Nope :(")
        quit()
else:
    print("Create a new master password to keep all your data")
    user = input("Enter = ")
    store_master(user)
    main()
