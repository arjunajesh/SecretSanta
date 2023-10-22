from email.message import EmailMessage
import sys
import csv
import ssl
import smtplib
import random
my_email = sys.argv[1]
password = sys.argv[2]

people = []

with open(sys.argv[3], 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        people.append((line[0], line[1]))

def send_email(gifter_email, gifter_name, recipient_name):
    m = EmailMessage()
    m['From'] = my_email
    m['To'] = gifter_email
    m['subject'] = f"{gifter_name} - Secret Santa"
    m.set_content(f"Your giftee is {recipient_name}")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(my_email, password)
        smtp.sendmail(my_email, gifter_email, m.as_string())

random.shuffle(people)
gifter, gifter_email = people[0]
while people:
    giftee, giftee_email = people.pop()
    send_email(gifter_email, gifter, giftee)
    gifter, gifter_email = giftee, giftee_email


