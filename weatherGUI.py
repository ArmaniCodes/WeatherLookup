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


    #Setup the Window, Title, And Search Button
    def setUpGui(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.root.resizable(False,False)
        self.root.title("Weather Lookup")
        self.root.geometry('500x400')
        self.root.wm_iconbitmap("3721962.ico")

        guiTitle = ctk.CTkLabel(self.root,text="Weather Lookup", font=("Arial",15))
        guiTitle.pack()

        #Variable to store textBox text
        self.city_input = tk.StringVar()
        city_entry = ctk.CTkEntry(self.root,textvariable= self.city_input)

        #Button to search
        self.city_entryb = ctk.CTkButton(self.root,  text = "Search Weather", fg_color="#85338F", command = self.searchCity)

        city_entry.pack()
        self.city_entryb.pack(pady=10)


