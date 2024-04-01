import {forecast, temp_unit} from './store.js'
import {get} from 'svelte/store'

/**
 * This function fetches weather data for a given city from an API and updates the 'forecast' store with the response.
 * If there is an error during the API call, it sets the 'forecast' store to null and logs the error.
 * @param {string} city_name - The name of the city for which weather data is to be fetched.
 */
export const get_city_weather = async (city_name) => {
    console.log("Getting city ", city_name);

    window.client_api.get_weather(city_name)
        .then(response => {
            forecast.set(response.data);
        }).catch(reason => {
            forecast.set(null);
            console.error(reason);
            alert(JSON.stringify(reason.response.data));
        })
}

/**
 * This function pads a number with a leading zero if it is less than 10.
 * @param {number} number - The number to be padded.
 * @returns {string} - The padded number as a string.
 */
function padZero(number) {
    return (number < 10 ? '0' : '') + number;
}

/**
 * This function converts temperature from Kelvin to Celsius or Fahrenheit based on the selected unit.
 * @param {number} temp - The temperature value to be converted (in Kelvin).
 * @returns {string} - The converted temperature as a string with one decimal point.
 * @throws {Error} - If an invalid temperature unit is stored in 'temp_unit'.
 */
export const convertTemp = (temp) => {
    let toUnit = get(temp_unit);
    switch (toUnit) {
        case "C":
            return (temp - 273.15).toFixed(1);
        case "F":
            return ((temp - 273.15) * (9 / 5) + 32).toFixed(1);
        default:
            throw new Error("Invalid value stored in temp");
    }
};

/**
 * This function converts a Unix timestamp to adjusted time based on the given time zone offset.
 * @param {number} unix_timestamp - The Unix timestamp to be converted.
 * @param {number} timeZoneOffset - The offset in seconds (e.g., -14400 for UTC-4).
 * @returns {string} - The adjusted time in HH:mm format.
 */
export const get_time = (unix_timestamp, timeZoneOffset) => {

    // var timeZoneOffset is the offset in seconds (e.g., -14400 for UTC-4)

    // Convert the timestamp to milliseconds
    const timestampMilliseconds = unix_timestamp * 1000;

    // Create a new Date object with the adjusted time based on the offset
    const date = new Date(timestampMilliseconds + timeZoneOffset * 1000);

    // Extract the hour and minute components from the adjusted date
    const hours = date.getHours();
    const minutes = date.getMinutes();

    // Format the adjusted time as a string
    return padZero(hours) + ':' + padZero(minutes);
}
