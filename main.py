import requests

OMW_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "b9aff343ed1510c1239bf0222579d4cb"


weather_params = {
    "lat" : 23.014509,
    "lon": 72.591759,
    "appid" : api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(OMW_Endpoint,params=weather_params)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data["hourly"][:12]


will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("bring an umbrella")
# print(weather_data["hourly"][0]["weather"][0]["id"])

