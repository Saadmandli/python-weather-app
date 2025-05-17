import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "3291a9e472022a78a96b0243bf732def"
account_sid = "ACd1fe442255542664b934c11e78cab64b"
auth_token = "31a5b11b52943d61ebafe5442d6a8503"

parameters = {
    "lat": 22.975889,
    "lon": 72.497627,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today, Bring your Umbrella ☂️",
        from_="whatsapp:+14155238886",
        to="whatsapp: your number",
    )
    print(message.status)
