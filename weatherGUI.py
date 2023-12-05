import tkinter as tk
import customtkinter as ctk
from request import getCityWeather


class WeatherGui:
    def __init__(self):
        self.root = ctk.CTk()
        self.visualized = False
        self.root.mainloop()


