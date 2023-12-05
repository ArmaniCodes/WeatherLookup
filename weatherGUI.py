import tkinter as tk
import customtkinter as ctk
from request import getCityWeather


class WeatherGui:
    def __init__(self):
        self.root = ctk.CTk()



        #Used to check if the main Frame is visualized
        self.visualized = False

        self.setUpGui()

        #main loop that runs the GUI
        self.root.mainloop()


    def setUpGui(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.root.resizable(False,False)
        self.root.title("Weather Lookup")
        self.root.geometry('500x400')
        self.root.wm_iconbitmap("3721962.ico")


