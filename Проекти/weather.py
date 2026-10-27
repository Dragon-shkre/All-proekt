import requests as rq
import tkinter as tk

window = tk.Tk()
window.config(bg="#87CEEB")


window.title("Прогноз погоды")
window.geometry("400x300")


title = tk.Label(window, text="Прогноз погоды", font=("Arial", 20))
title.pack()


city_input = tk.Entry(window, width=25, bg="white")
city_input.pack(pady=10)


weather_frame = tk.Frame(window, bg="white")
weather_frame.pack(pady=20)


weather_label = tk.Label(
    weather_frame,
    text="",
    bg="white",
    font=("Arial", 14)
)


weather_label.pack(padx=30, pady=15)


def get_weather_description(code):
    if code == 0:
        return "☀️ Ясно"
    elif code in [1, 2, 3]:
        return "☁️ Облачно"
    elif code in [45, 48]:
        return "🌫 Туман"
    elif code in [51, 53, 55, 56, 57]:
        return "🌦 Морось"
    elif code in [61, 63, 65, 66, 67]:
        return "🌧 Дождь"
    elif code in [71, 73, 75, 77]:
        return "❄️ Снег"
    elif code in [80, 81, 82]:
        return "🌦 Ливень"
    elif code in [95, 96, 99]:
        return "⛈ Гроза"
    else:
        return "❓ Неизвестно"


def get_weather():
    city = city_input.get()

    if not city:
        weather_label.config(text="Введите город ❗")
        return

    geo_url = "https://geocoding-api.open-meteo.com/v1/search"

    geo_params = {
        "name": city,
        "count": 1,
        "language": "ru",
        "format": "json"
    }

    # Получаем координаты города
    try:
        geo_response = rq.get(geo_url, params=geo_params)
        geo_data = geo_response.json()
    except Exception as error:
        print(error)
        weather_label.config(text="Ошибка соединения ❌")
        return

    # Проверяем, найден ли город
    if "results" not in geo_data or not geo_data["results"]:
        weather_label.config(text="Город не найден ❌")
        return

    latitude = geo_data["results"][0]["latitude"]
    longitude = geo_data["results"][0]["longitude"]
    city_name = geo_data["results"][0]["name"]

    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m,weather_code",
        "daily": "temperature_2m_max,temperature_2m_min,weather_code",
        "forecast_days": 7
    }

    # Получаем погоду
    try:
        weather_response = rq.get(weather_url, params=weather_params)
        weather_data = weather_response.json()


        temperature = weather_data["current"]["temperature_2m"]
        wind_speed = weather_data["current"]["wind_speed_10m"]
        weather_code = weather_data["current"]["weather_code"]

        weather_description = get_weather_description(weather_code)

        daily = weather_data["daily"]

        dates = daily["time"]
        max_temperatures = daily["temperature_2m_max"]
        min_temperatures = daily["temperature_2m_min"]
        weather_codes = daily["weather_code"]

    except Exception as error:
        print(error)
        weather_label.config(text="Не удалось получить погоду ❌")
        return
    forecast_text = ""

    for i in range(7):
        description = get_weather_description(weather_codes[i])

        forecast_text += (
            f"{dates[i]} | "
            f"{description} | "
            f"{min_temperatures[i]}°C / {max_temperatures[i]}°C\n"
        )
    # Выводим результат
    weather_label.config(
        text=f"📍 {city_name}\n\n"
             f"{weather_description}\n"
             f"🌡 Сейчас: {temperature}°C\n"
             f"💨 Ветер: {wind_speed} км/ч\n\n"
             f"ПРОГНОЗ НА 7 ДНЕЙ:\n"
             f"{forecast_text}"
    )



button = tk.Button(window, text="Узнать погоду", command=get_weather)
button.pack()


window.mainloop()