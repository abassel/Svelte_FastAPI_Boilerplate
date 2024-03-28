# Weather App
A weather app that caches its data from the OpenWeatherMap API

## Run the stack 

Create a `.env` file with the following contents
```dotenv
DEV=true
WEATHER_API_KEY=<OPENWEATHERMAP_KEY>
```

Then run the command below:

```bash
docker-compose up --build  # might want to add -d to run detached 
```
