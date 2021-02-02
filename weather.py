from tkinter import * 
import requests 
from datetime import datetime 



class Weather:
    """Get Weather for a NYC by day"""

    def __init__(self):
        
        self.parameters = {"lat": 40.678177,
              "lon": -73.944160,
              "appid": "218b24d7ce6304b960ea72f565d4a9c9",
              "units": "imperial",
              "exclude": "hourly,minutely"}
        self.res = requests.get(
            "https://api.openweathermap.org/data/2.5/onecall", params=self.parameters)
        self.data = self.res.json()
        self.current_data = self.data["current"]
        self.date = self.current_data["dt"]
        self.date = self.data
        self.current_temp = round(self.current_data["temp"])
        self.weather_id = self.current_data["weather"][0]["id"]
        self.weather = self.weather_con(self.weather_id)
        

    def weather_con(self, weather_id):
        """Return the weather conditions for the day based on self.weather_id"""
        self.weather_id = self.weather_id
        if self.weather_id in range(200, 233):
            return "Thunderstorm"
        elif self.weather_id in range(300, 325):
            return "Drizzle"
        elif self.weather_id in range(500, 535):
            return "Rain"
        elif self.weather_id in range(600, 625):
            return "Snow"
        elif self.weather_id in range(801, 805):
            return "Clouds"
        elif self.weather_id == 800:
            return "Clear"

    def weekly_weather(self):
        self.weekly_data = self.data["daily"]
        self.week_dict = {}
        for day in self.weekly_data:
            timestamp = day["dt"]
            weekday = datetime.utcfromtimestamp(timestamp).strftime('%A')
            self.week_dict[weekday] = day 
        return self.week_dict
    
   


        
         






