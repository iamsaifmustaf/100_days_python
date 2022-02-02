from random import random
import smtplib
from urllib.parse import quote_plus
import datetime as dt
import random


quotes = open("./quotes.txt","r")
quotes_array = quotes.read().split("\n")


email_1 = "ameeralazzawi92@gmail.com"
password_1 = "@PPle1234"

week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email_1, password=password_1)
    connection.sendmail(
        from_addr=email_1,
        to_addrs="hansolo9292@protonmail.com",
        msg=f"Subject:{week[dt.datetime.now().weekday()]}\n\n{quotes_array[random.randint(0,len(quotes_array) - 1)]}"
    )




