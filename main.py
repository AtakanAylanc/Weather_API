import requests

# Enter your API key here
api_key = "71b4b3d75892e7f76bfaae33da137e5d"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
city_name = input("Enter city name : ")

# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()

# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":

    print(x)
    # store the value of "main"
    # key in variable y
    y = x["main"]

    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]

    # store the value corresponding
    # to the "pressure" key of y
    current_temp_max = y["temp_max"]

    # store the value corresponding
    # to the "humidity" key of y
    current_temp_min = y["temp_min"]

    # store the value of "weather"
    # key in variable z
    z = x["weather"]

    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]

    # print following values
    print(" Temperature = " +
          str(current_temperature - 273.15) +
          "\n maximum temperature = " +
          str(current_temp_max - 273.15) +
          "\n minimum temperature = " +
          str(current_temp_min - 273.15) +
          "\n description = " +
          str(weather_description))

else:
    print(" City Not Found ")