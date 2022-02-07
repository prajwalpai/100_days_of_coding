import datetime
import requests
import os
from twilio.rest import Client

local_datetime = datetime.datetime.now()
local_datetime_timestamp = float(local_datetime.strftime("%s"))

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)



PARAMS={
    'lat':'1.2522',
    'lon':'113.5729',
    'exclude':'current,minutely,daily',
    'appid':"b10d97ccae349e57f5479a367bf317f6",
    'units':'metric'
}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall?",params=PARAMS)
lookout_for=['Thunderstorm','Drizzle', 'Rain', 'Clouds']
will_rain = False

for dat in response.json()['hourly'][:12]:
    date = datetime.datetime.fromtimestamp(dat['dt'])
    temparature=dat['temp']
    id_weather = dat['weather'][0]['id']
    main_weather = dat['weather'][0]['main']
    #print(f"{date} - {temparature} - {main_weather}")
    if id_weather < 700 :
        will_rain = True

if will_rain:
    message = client.messages \
        .create(
        body="It is gonna rain!! Do carry an Umberella",
        from_='+19035737818',
        to='+919916555594'
    )
    print(message.sid)
