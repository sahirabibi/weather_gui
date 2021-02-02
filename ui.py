from tkinter import *
from weather import Weather

ICON_COLOR = "#70a0bc"
BG_COLOR = "#7aa4bc"
TXT_COLOR = "#ddf3f5"
days_of_week = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
weather_icons = {
    "Clear": "weather_icons/sunshine.png",
    "Clouds": "weather_icons/cloudy.png",
    "Snow": "weather_icons/snow.png",
    "Rain": "weather_icons/rain.png"
}


class App:

    def __init__(self, window):
        self.current = Weather()
        self.today = self.current.weekly_weather()
        self.window = window
        window.title("NYC Weather")
        window.config(padx=50, pady=50, bg=BG_COLOR)
        self.canvas = Canvas(height=400, width=400,
                             highlightthickness=0, bg=ICON_COLOR)
        self.icon_img = PhotoImage(file=weather_icons[self.current.weather])
        self.canvas.create_image(200, 100, image=self.icon_img)
        self.canvas.create_text(200, 40, text="New York City", font=(
            "Courier", 40, "normal"), fill="#ddf3f5")
        self.canvas.create_text(210, 170, text=f"{self.current.current_temp}°", font=(
            "Courier", 50, "normal"), fill="#ddf3f5")
        self.canvas.create_text(200, 210, text=self.current.weather, font=(
            "Courier", 30, "normal"), fill="#ddf3f5")
        self.canvas.create_text(200, 240, text=f"H:35 L: 19", font=(
            "Courier", 20, "normal"), fill="#ddf3f5")
        self.canvas.grid(row=0, column=0, rowspan=3)
        self.change_city = Button(text="Change City")
        self.change_city.grid(row=2, column=0)

        window.mainloop()

        