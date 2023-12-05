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



    #Devisualize error Box and grab parsed info
    #If parsed Info then visualize and apply Info
    def searchCity(self):
        self.error.grid_forget()
        city = self.city_input.get() #This grabs the user Input from the textBox
        info = getCityWeather(city)
        if info is None:
            self.devisualizeItems()
            return
        if not self.visualized:
            self.visualizeItems()
        self.applyInfo(info)

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
    #anchor = "w" makes it so it stays attached on X
    #We don't pack (visualize) them yet. Only visualize once a city is searched
    def setUpWeatherFrame(self):
        self.frame = ctk.CTkFrame(self.root,border_width=1)
        self.frame.pack(pady=20,padx=60,fill="both",expand=True)
        self.weatherImage = tk.Label(self.frame,anchor="w")
        self.location = tk.Label(self.frame, text="Location:", background="gray13", foreground="white", anchor="w")
        self.error = tk.Label(self.frame, text="Error: Invalid City or Timeout! Try Again.", background="gray13",foreground="white", anchor="w")
        self.timeZone = tk.Label(self.frame, text="Timezone:", background="gray13", foreground="white", anchor="w")
        self.localTime = tk.Label(self.frame, text="Local Time:", background="gray13", foreground="white", anchor="w")
        self.temperature = tk.Label(self.frame, text="Temperature:", background="gray13", foreground="white",anchor="w")
        self.status = tk.Label(self.frame, text="Status:", background="gray13", foreground="white", anchor="w")
        self.precipitation = tk.Label(self.frame, text="Precipitation:", background="gray13", foreground="white",anchor="w")
        self.Humidity = tk.Label(self.frame, text="Humidity:", background="gray13", foreground="white", anchor="w")


    #Visualizes items in frame when a correct city is searched!
    #Using .grid instead of .pack to ensure a tidy layout
    def visualizeItems(self):
        self.visualized = True
        self.weatherImage.grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.location.grid(row=1, column=0, padx=15, pady=2, sticky="w")
        self.timeZone.grid(row=2, column=0, padx=15, pady=2, sticky="w")
        self.localTime.grid(row=3, column=0, padx=15, pady=2, sticky="w")
        self.temperature.grid(row=4, column=0, padx=15, pady=2, sticky="w")
        self.status.grid(row=6, column=0, padx=15, pady=2, sticky="w")
        self.precipitation.grid(row=7, column=0, padx=15, pady=2, sticky="w")
        self.Humidity.grid(row=8, column=0, padx=15, pady=2, sticky="w")


    #Devisualizes items for when there is an error
    #Loops through the children of the Frame and grid_forgets it which devisualizes it
    def devisualizeItems(self):
        self.visualized = False
        for i in self.frame.winfo_children():
            i.grid_forget()
        self.error.grid(row=1, column=0, padx=15, pady=2, sticky="w")



    #Takes the info from the parsed Json response and uses it to apply it
    def applyInfo(self,info):
        self.weatherImage.config(image=info["Image"])
        self.weatherImage.image = info["Image"]
        self.location.config(text="Location: \t" + info["Location"])
        self.timeZone.config(text="Timezone: \t" + info["Timezone"])
        self.localTime.config(text="Local Time: \t" + info["LocalTime"])
        self.temperature.config(text="Temperature: \t" + str(info["Temperature"]) + " Celcius")
        self.status.config(text="Status: \t\t" + info["Status"])
        self.precipitation.config(text="Precipitation: \t" + str(info["Precipitation"]))
        self.Humidity.config(text="Humidity: \t" + str(info["Humidity"]))
