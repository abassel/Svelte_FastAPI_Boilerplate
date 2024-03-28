import json

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import requests
import redis

from .config import app_config, LOG


redis_cache = redis.Redis(host='redis', port=6379, db=0)


def get_weather(city: str):

    city = city.strip().lower()

    # Try to get data from redis cache
    str_json = redis_cache.get(city)
    if str_json:
        json_dict = json.loads(str_json)
        LOG.warning("Using cache")
        return json_dict

    LOG.debug(f"Reaching to openweathermap for city {city}")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={app_config.WEATHER_API_KEY}'

    response = requests.get(url)
    if response.status_code != 200:
        LOG.error(f'Error fetching weather data: {response.text}')

    json_data = response.json()

    redis_cache.set(city, json.dumps(json_data), app_config.CACHE_TTL_SECONDS)
    return json_data


app = FastAPI()


@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url="/docs")


@app.get("/weather/{city}")
async def weather_endpoint_get(city: str):
    return get_weather(city=city)

