from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import requests

from .config import app_config, LOG


def get_weather(city: str):

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={app_config.WEATHER_API_KEY}'

    response = requests.get(url)
    if response.status_code != 200:
        LOG.error(f'Error fetching weather data: {response.text}')

    json_data = response.json()

    return json_data


app = FastAPI()


@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url="/docs")


@app.get("/weather/{city}")
async def weather_endpoint_get(city: str):
    return get_weather(city=city)

