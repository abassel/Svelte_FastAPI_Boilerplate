import json

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import requests
import redis

from .config import app_config, LOG


redis_cache = redis.Redis(host='redis', port=6379, db=0)

app = FastAPI(root_path="/api")

def get_weather(city: str):
    """
    Fetches weather data for a given city from OpenWeatherMap API.

    Args:
        city (str): The name of the city for which weather data is requested.

    Returns:
        dict: A dictionary containing weather data for the specified city.
    """

    LOG.debug(f"Reaching to openweathermap for city {city}")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={app_config.WEATHER_API_KEY}'

    try:
        response = requests.get(url)
    except Exception as e:
        LOG.exception(e)
        # Do not expose stack trace to client
        raise HTTPException(status_code=500, detail=f"Internal server error.")

    if response.status_code != 200:
        LOG.error(f'Error fetching weather data: {response.text}')
        raise HTTPException(status_code=response.status_code, detail=f"Failed to fetch weather data -> {response.text}")

    json_data = response.json()

    return json_data


@app.get("/", include_in_schema=False)
async def docs_redirect():
    """
    Redirects the root URL to the API documentation.
    """
    return RedirectResponse(url="/api/docs")


@app.get("/weather/{city}", operation_id="get_weather")
async def weather_endpoint_get(city: str):
    """
    Endpoint to retrieve weather data for a specific city.
    Will return cached data if requested city is found in Redis

    Args:
        city (str): The name of the city for which weather data is requested.

    Returns:
        dict: A dictionary containing weather data for the specified city.
    """
    city = city.strip().lower()

    # Try to get data from redis cache
    str_json = redis_cache.get(city)
    if str_json:
        json_dict = json.loads(str_json)
        LOG.warning("Using cache")
        return json_dict

    json_dict = get_weather(city=city)
    redis_cache.set(city, json.dumps(json_dict), app_config.CACHE_TTL_SECONDS)

    return json_dict
