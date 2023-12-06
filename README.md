## Weather Lookup

Want to search up weather across the world? This python program uses the API WeatherStack to retrieve weather info from cities all over the world. It then displays this information using the GUI Interface Tkinter.
## Installation
Clone this repo
```sh
git clone "https://github.com/ArmaniCodes/WeatherLookup/"
```

## Dependencies
Pillow, customtkinter, Requests,Packaging. To download them simply run: 
```sh
pip install -r requirements.txt
```
## APIKEY
To use this program you need to signup on WeatherStack.com to retrieve a free API KEY. Once you signup head to your dashboard where you will locate your free API key. Then create a file named config.py in the project directory and place
```sh
apiKey = "YOURKEY"
```
Inside! Alternatively you can just place your apikey inline in request.py

## Usage
Simply type the name of the city in the textbox and click the search button to retrieve the weather information. Misspelled the name of the city? No worries the API will most likely know which city you meant.

## Preview
![image](https://github.com/ArmaniCodes/WeatherLookup/assets/103855175/7d96b105-f054-4ffa-8e57-ba24ee0705bc)
