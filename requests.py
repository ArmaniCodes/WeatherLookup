import requests
import config


apiK = config.apiKey
apiURL = "http://api.weatherstack.com/current"
params = {  f"access_key" : {apiK} ,
            "query":""}
