"""Weather CLI
"""
import json
import os
import sys
import requests

from clize import run


if os.environ.get('API_KEY') is None:
    print("API_KEY environment variable is not set!")
    sys.exit(-1)

try:
    PUBLIC_IP = requests.get("https://api.ipify.org", timeout=30).text
except requests.RequestException as e:
    print(f"Error retrieving public IP address: {e}")
    PUBLIC_IP = None


API_KEY = os.environ.get('API_KEY')
DEBUG_WEATHER = os.environ.get('DEBUG_WEATHER', False)
URL = "https://api.weatherapi.com/v1/forecast.json"
API_URL = f"{URL}?key={API_KEY}&q={PUBLIC_IP}&days=1&aqi=no&alerts=no"


def rain():
    """Discovery if today the chance of rain is greater than 5%
    """
    output = False
    forecast = requests.get(API_URL, timeout=30)
    parsed = json.loads(forecast.content)["forecast"]["forecastday"][0]["day"]

    if parsed["daily_chance_of_rain"] > 5:
        output = True

    if DEBUG_WEATHER:
        return f"""
        ====== DEBUG MODE ENABLED ======
        Your Public IP is {PUBLIC_IP}
        The chance of rain is {parsed["daily_chance_of_rain"]}%
        Is today will rain? {output}
        """
    return output

def shine():
    """Discovery if today the chance of UV is greater than 3
    """
    output = False
    forecast = requests.get(API_URL, timeout=30)
    parsed = json.loads(forecast.content)["forecast"]["forecastday"][0]["day"]

    if parsed["uv"] > 3:
        output = True

    if DEBUG_WEATHER:
        return f"""
        ====== DEBUG MODE ENABLED ======
        Your Public IP is {PUBLIC_IP}
        The uv is {parsed["uv"]}
        Is today will be a shiny day? {output}
        """

    return output


if __name__ == '__main__':
    run(rain, shine, description="""
        A simple weather command line to check rain and shine conditions

        Required |- set API_KEY environment variable before use it

        Optional |- set DEBUG_WEATHER environment variable as True to enable debug mode
        """)
