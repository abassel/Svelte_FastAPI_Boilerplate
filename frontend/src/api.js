
import {forecast} from './store.js'


export const get_city_weather = async (city_name) => {
    console.log("Getting city ", city_name);
    let res = await window.client_api.get_weather(city_name);
    console.log(res);

    forecast.set(res.data);
    // Clear up and log error
    if (res.data.cod !== 200 ){
        forecast.set(null);
        console.error(res.data);
        alert(JSON.stringify(res.data));
    }
}
