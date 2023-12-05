import requests
import config
from io import BytesIO
from PIL import Image, ImageTk

apiK = config.apiKey
apiURL = "http://api.weatherstack.com/current"
params = {  f"access_key" : {apiK} ,
            "query":""}


#Update image because the API returns the status image as a link which is not compatible with TKinter
def updateImage(Layout):
    imageResponse = requests.get(Layout["Image"])

def checkResponse(response):
    #if the string success appears in the Json we know it failed.
    print(response.json())
    if "success" in response.json() or response.status_code != 200:
        return None

    #if successful parse info and return it as a dictionary
    if response.status_code == 200 and "success" not in response:
        data = response.json()
        Layout = {
            "Location" : data["location"]["name"] + "," + data["location"]["country"],
            "Timezone": data["location"]["timezone_id"],
            "LocalTime": data["location"]["localtime"].split()[-1],
            "Temperature":  data["current"]["temperature"],
            "Status": data["current"]["weather_descriptions"][0],
            "Precipitation": data["current"]["precip"],
            "Humidity": data["current"]["humidity"],
            "Image": data["current"]["weather_icons"][0]
        }

    return Layout

def getCityWeather(City):
    params["query"] = City
    response = requests.get(apiURL,params=params)
    return checkResponse(response)