import requests
from datetime import datetime
import tkinter as tk

def get_weather():
    city_name = city_entry.get()
    API_key = '103069ce87586acba31251c354fffcfd'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        sunrise_time = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')
        sunset_time = datetime.fromtimestamp(data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')
        
        weather_info = f"""
        Weather is: {data['weather'][0]["description"]}
        Current temperature is: {data['main']['temp']}°C
        Temperature feels like: {data['main']['feels_like']}°C
        Humidity: {data['main']['humidity']}%
        Wind speed: {data['wind']['speed']} m/s
        Pressure: {data['main']['pressure']} hPa
        Visibility: {data['visibility']} meters
        Sunrise: {sunrise_time}
        Sunset: {sunset_time}
        """
        weather_label.config(text=weather_info)
    elif response.status_code == 404:
        weather_label.config(text="City not found. Please check the city name and try again.")
    else:
        weather_label.config(text=f"Failed to retrieve data. Status code: {response.status_code}")


root = tk.Tk()
root.title("Weather App")


root.configure(bg='lightblue')
font_style = ("Helvetica", 14)


tk.Label(root, text="Enter the city name:", font=font_style, bg='lightblue').pack(pady=10)
city_entry = tk.Entry(root, font=font_style, width=30)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather, font=font_style, bg='white').pack(pady=20)


weather_label = tk.Label(root, font=font_style, bg='lightblue', justify=tk.LEFT)
weather_label.pack(pady=10)

root.mainloop()

