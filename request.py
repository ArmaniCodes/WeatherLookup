import requests
import config


apiK = config.apiKey
apiURL = "http://api.weatherstack.com/current"
params = {  f"access_key" : {apiK} ,
            "query":""}


def getCityWeather(City):
    params["query"] = City
    response = requests.get(apiURL,params=params)
    print(reponse.json())

getCityWeather("New York")