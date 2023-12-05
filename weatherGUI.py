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


    def searchCity(self):
        city = self.city_input.get()
        info = getCityWeather(city)
        if info is None:
            print("Error")
            return
        else:
            print(info)

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
        self.setUpWeatherFrame()

    #Sets up the frame that has the weather information
    def setUpWeatherFrame(self):
        self.frame = ctk.CTkFrame(self.root,border_width=1)
        self.frame.pack(pady=20,padx=60,fill="both",expand=True)


