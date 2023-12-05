import requests
import config


apiK = config.apiKey
apiURL = "http://api.weatherstack.com/current"
params = {  f"access_key" : {apiK} ,
            "query":""}


def checkResponse(response):
    if "success" in response.json() or response.status_code != 200:
        return None


def getCityWeather(City):
    params["query"] = City
    response = requests.get(apiURL,params=params)
    return checkResponse(response)