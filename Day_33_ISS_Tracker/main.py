import requests
from datetime import datetime
import smtplib

MY_LAT = 12.971599
MY_LONG = 77.594566

my_email = "prajwalpai.forcourse@yahoo.com"
password = 'jtcdkbfdhgejtmbw'

#Your position is within +5 or -5 degrees of the ISS position.
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_latitude,iss_longitude)
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and  MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    else:
        return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 5
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 6

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


if is_iss_overhead():
    print(sunrise,time_now.hour,sunset)
    if sunrise >= time_now.hour or time_now.hour >= sunset:
        print("Sending mail")
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs='prajwal.pai@gmail.com',
                msg='Subject: Look up the sky!\n\n The ISS is flying by , time to say Hi'
            )
else:
    print("ISS is far away!")

