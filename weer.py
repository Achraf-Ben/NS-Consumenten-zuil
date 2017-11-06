import forecastio

api_key = "dca7849ad2985d67e63bdce010c191ee"
# Utrecht
latitude = 52.0884851
longitude = 5.1180588

forecast = forecastio.load_forecast(api_key, lat, lng)
byHour = forecast.daily()
print(byHour.summary)
print(byHour.icon)


# https://pypi.python.org/pypi/python-forecastio/
#
