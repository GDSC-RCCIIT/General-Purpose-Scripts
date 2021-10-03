# importing required packages
import requests
import hashlib
import sys


# API requires first 5 characters of the password and fetches the full list of passwords
# that were breached starting from those first 5 letters
# this way you don't need to send your full password and can get the appropriate data locally
# that is why this script is more secure than manually going to the website and typing out your password their
def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if (
        res.status_code != 200
    ):  # if res.status_code is not 200 then there is some problem
        raise RuntimeError(
            f"Error fetching: {res.status_code}, check the API and try again."
        )
    return res


# function to get the data of you password by matching your password with the fetched list
def get_password_leak_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def password_api_check(password):
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(
        first5_char
    )  # list of all the passwords fetched from the API starting from first 5 letters
    return get_password_leak_count(response, tail)


def main(args):
    for password in args:
        count = password_api_check(password)
        if count:
            print(
                f"{password} was found {count} times... you should probably change it!"
            )
        else:
            print(f"{password} was NOT found. Carry on!")
    return "done!"


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))  # takes multiple arguments
