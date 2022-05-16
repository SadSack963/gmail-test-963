import smtplib
import datetime as dt
import random
import os
from dotenv import load_dotenv


def random_quote():
    with open("quotes.txt", encoding="utf-8") as file:
        list_quote = file.readlines()
    return random.choice(list_quote)


def send_mail_gmail(day, quote):
    # GMAIL
    GMAIL_SENDER = os.getenv("SMTP_GMAIL_SENDER")
    GMAIL_USERNAME = os.getenv("SMTP_GMAIL_USERNAME")
    GMAIL_EMAIL = os.getenv("SMTP_GMAIL_EMAIL")
    # GMAIL_PASSWORD = os.getenv("SMTP_GMAIL_PASSWORD")
    GMAIL_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
    GMAIL_RECIPIENT = os.getenv("SMTP_GMAIL_RECIPIENT")

    message = f"From: \"{GMAIL_SENDER}\" <{GMAIL_EMAIL}>\n" \
              f"To: {GMAIL_RECIPIENT}\n" \
              f"Subject: Quote of the day\n\n" \
              f"{day} Motivation\n{quote}".encode("utf-8")
    print(message)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.set_debuglevel(1)  # Set the debug level
        connection.starttls()  # encrypt following SMTP commands
        connection.login(user=GMAIL_USERNAME, password=GMAIL_PASSWORD)  # could also use user=GMAIL_EMAIL
        connection.sendmail(from_addr=GMAIL_EMAIL, to_addrs=GMAIL_RECIPIENT, msg=message)


# Used to retrieve Environment Variables from file
load_dotenv("E:/Python/EnvironmentVariables/.env")

# set a datetime object
# dob = dt.datetime(year=1955, month=8, day=5)

now = dt.datetime.now()
day_of_week = now.strftime("%A")

quote_of_the_day = random_quote()

send_mail_gmail(day_of_week, quote_of_the_day)
