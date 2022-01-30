import random
import smtplib
import datetime as dt

my_email = "prajwalpai.forcourse@yahoo.com"
password = 'jtcdkbfdhgejtmbw'

with open('quotes.txt', 'r') as file:
    quote_list = file.readlines()

now=dt.datetime.now()

if now.weekday() == 6:
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='prajwal.pai@gmail.com',
            msg='Subject: Monday Quote\n\n'+random.choice(quote_list)
        )

