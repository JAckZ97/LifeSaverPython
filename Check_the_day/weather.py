import pyowm
import emoji

# You MUST provide a valid API key
owm = pyowm.OWM('63ec788a1183c4324606312c792fc5b1')

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)
observation = owm.weather_at_place('Montreal,CA')
w = observation.get_weather()

print(w)
# <Weather - reference time=2013-12-18 09:20,
# status=Clouds>

# Weather details
print(w.get_wind())           # {'speed': 4.6, 'deg': 330}
print(w.get_humidity())             # 87
print(w.get_weather_icon_url())  # Get weather-related icon URL
# {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print(w.get_temperature('celsius'))


print(emoji.emojize('Python is :thumbs_up:'))
