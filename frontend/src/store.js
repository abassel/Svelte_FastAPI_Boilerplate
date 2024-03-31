// Ref
// https://svelte.dev/repl/a551a40e90374fd2861255c957123af2?version=3.22.2

import {writable} from 'svelte/store'

export const forecast = writable(null);

export const temp_unit = writable("F");

export const fake_data = {
    "coord": {
        "lon": -81.3792,
        "lat": 28.5383
    },
    "weather": [
        {
            "id": 803,
            "main": "Clouds",
            "description": "broken clouds",
            "icon": "04d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 295.27,
        "feels_like": 295.47,
        "temp_min": 293.58,
        "temp_max": 296.9,
        "pressure": 1022,
        "humidity": 74
    },
    "visibility": 10000,
    "wind": {
        "speed": 1.79,
        "deg": 322,
        "gust": 2.24
    },
    "clouds": {
        "all": 75
    },
    "dt": 1711896091,
    "sys": {
        "type": 2,
        "id": 2084244,
        "country": "US",
        "sunrise": 1711883756,
        "sunset": 1711928566
    },
    "timezone": -14400,
    "id": 4167147,
    "name": "Orlando",
    "cod": 200
};
