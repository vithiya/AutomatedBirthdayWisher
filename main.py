##################### Extra Hard Starting Project ######################
import pandas
from numpy.core.records import record
import datetime as dt
import random
import smtplib

my_email="vithiyaofficial@gmail.com"
password="usbnckisyhtqfecr"
today=(dt.datetime.now().month,dt.datetime.now().day)
birthday_info=pandas.read_csv("birthdays.csv")
birthday_dict={(data_row["month"],data_row["day"]):data_row for (index,data_row) in birthday_info.iterrows()}

if today in birthday_dict:
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content=letter_file.read()
        birthday_wish=content.replace("[NAME]",birthday_dict[today]["name"])

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=birthday_dict[today]["email"],msg=f"Subject:Happy Birthday\n\n{birthday_wish}")




