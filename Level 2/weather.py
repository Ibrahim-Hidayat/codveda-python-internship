import requests

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

def get_coordinates(city):
    try:
        response = requests.get(GEOCODE_URL, params={"name": city, "count": 1}, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error contacting the server: {e}")
        return None
    except ValueError:
        print("Error: The server sent an invalid response.")
        return None

    results = data.get("results")
    if not results:
        print(f"City '{city}' was not found.")
        return None

    place = results[0]
    return place["latitude"], place["longitude"], place["name"], place.get("country", "")

def get_weather(lat, lon):
    params = {"latitude": lat, "longitude": lon, "current_weather": "true"}
    try:
        response = requests.get(WEATHER_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()["current_weather"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather: {e}")
    except (ValueError, KeyError):
        print("Error: The weather data was in an unexpected format.")
    return None

def main():
    city = input("Enter a city name: ").strip()
    if not city:
        print("City name cannot be empty.")
        return

    location = get_coordinates(city)
    if location is None:
        return

    lat, lon, name, country = location
    weather = get_weather(lat, lon)
    if weather is None:
        return

    print(f"\nCurrent weather in {name}, {country}")
    print(f"Temperature: {weather['temperature']} °C")
    print(f"Wind speed:  {weather['windspeed']} km/h")
    print(f"Time:        {weather['time']}")

if __name__ == "__main__":
    main()