"""
Extract emails and phone numbers from the text clipboard input
or an input file and creates two csvs for it
"""
import re

import pandas as pd
import pyperclip


def email_phone_extractor(text):
    """
    Finds emails and phone numbers from text using regex
    :param text:
    :return:
    """
    email = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", text)
    phone_number = re.findall(r"[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]", text)
    return email, phone_number


def create_base_dataframes():
    """
    Creates two base dataframe for emails and phone numbers
    :return:
    """
    email_df = pd.DataFrame({"emails": []})
    phone_no_df = pd.DataFrame({"phone_no": []})
    return email_df, phone_no_df


def append_to_dataframe(data, list_of_values, which_list):
    """
    Append email and phone number to separate dataframes
    :return:
    """
    to_append = {which_list: list_of_values}
    data = data.append(pd.DataFrame(to_append))
    return data


def dataframe_to_csv(email_df, phone_no_df):
    """
    Writes two dataframes to csv
    """
    email_df.to_csv("emails.csv", index=False)
    phone_no_df.to_csv("phone_no.csv", index=False)


def read_a_txt(filename):
    """
    Reads a text file to Extract emails and phone numbers
    and creates two csvs for it
    :param filename: the text file name
    :return:
    """
    email_df, phone_no_df = create_base_dataframes()

    with open(filename, "r", encoding="UTF-8") as file:
        text = file.readlines()

    for line in text:
        email, no_ = email_phone_extractor(line)
        if len(email) > 0:
            email_df = append_to_dataframe(email_df, email, "emails")
        if len(no_) > 0:
            phone_no_df = append_to_dataframe(phone_no_df, no_, "phone_no")

    dataframe_to_csv(email_df, phone_no_df)


def extract_from_clipboard():
    """
    Reads from clipboard to Extract emails
    and phone numbers and creates two csvs for it
    :return:
    """
    email_df, phone_no_df = create_base_dataframes()
    text = str(pyperclip.paste())
    email, phone_number = email_phone_extractor(text)
    print(email, phone_number)
    if len(email) > 0:
        email_df = append_to_dataframe(email_df, email, "emails")
    if len(phone_number) > 0:
        phone_no_df = append_to_dataframe(phone_no_df, phone_number, "phone_no")
    dataframe_to_csv(email_df, phone_no_df)


if __name__ == "__main__":
    # extract_from_clipboard()
    read_a_txt(filename="test_emailno_extractor.txt")
