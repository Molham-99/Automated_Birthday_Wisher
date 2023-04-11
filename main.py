import pandas
import datetime as date
import random
import smtplib

my_email = "your email@*****.com"
password = "your password"

PLACEHOLDER = "[NAME]"
files = ['letter_templates/letter_1.txt', 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt']
file = random.choice(files)
data = pandas.read_csv("birthdays.csv")

now = date.datetime.now()
month = now.month
day = now.day
if day in data['day'].unique() and month in data['month'].unique():
    x = data[data.month == month]
    x_ls = x.name.to_list()
    y = data[data.day == day]
    y_ls = y.name.to_list()
    for n in x_ls:
        if n in y_ls:
            mail = data[data.name == n]
            t = mail.email
            email = t.to_string(index=False)
            with open(file) as letter:
                letter_contains = letter.read()
                new_letter = letter_contains.replace(PLACEHOLDER, n)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"subject: Happy Birthday\n\n{new_letter}")
