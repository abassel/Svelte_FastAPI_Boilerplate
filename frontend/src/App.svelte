<script>
    import OpenAPIClientAxios from 'openapi-client-axios';

    import {forecast, fake_data, temp_unit} from './store.js'

    import CloudRainIcon from './components/svg/CloudRainIcon.svelte';
    import SunriseIcon from './components/svg/SunriseIcon.svelte';
    import SunsetIcon from './components/svg/SunsetIcon.svelte';
    import WindIcon from './components/svg/WindIcon.svelte';
    import CitySearch from "./components/CitySearch.svelte";

    (async () => {
        // $forecast = fake_data;  // For debug without backend -> npm run dev
        const api = new OpenAPIClientAxios({definition: '/api/openapi.json'});
        window.client_api = await api.getClient();
        console.log("OpenApi client is ready!");
    })();

    function padZero(number) {
        return (number < 10 ? '0' : '') + number;
    }

    export const convertTemp = (temp) => {
        let toUnit = $temp_unit;
        switch (toUnit) {
            case "C":
                return (temp - 273.15).toFixed(1);
            case "F":
                return ((temp - 273.15) * (9 / 5) + 32).toFixed(1);
            default:
                throw new Error("Invalid value stored in temp");
        }
    };

    export const get_time = (unix_timestamp, timeZoneOffset) => {

        // var timeZoneOffset is the offset in seconds (e.g., -14400 for UTC-4)

        // Convert the timestamp to milliseconds
        var timestampMilliseconds = unix_timestamp * 1000;

        // Create a new Date object with the adjusted time based on the offset
        var date = new Date(timestampMilliseconds + timeZoneOffset * 1000);

        // Extract the hour and minute components from the adjusted date
        var hours = date.getHours();
        var minutes = date.getMinutes();

        // Format the adjusted time as a string
        var adjustedTime = padZero(hours) + ':' + padZero(minutes);

        return adjustedTime;
    }


</script>

<main>

    <div class="text-white min-vh-100 p-5">
        <div class="text-center">
            <CitySearch/>
        </div>
        {#if $forecast}
            <div class="text-center">
                <h1 class="display-4 font-weight-bold">{$forecast.name}</h1>
                <!--            <p class="h2">Sunday 4th August</p>-->
            </div>
            <div class="d-flex justify-content-center align-items-center my-4">
                <span class="font-weight-bold display-1">{convertTemp($forecast.main.temp)}°</span>
                <div class="text-right">
                    <p class="h4 font-weight-bold">{$forecast.weather[0].description}</p>
                    <p class="h3">
                        High <span class="font-weight-bold">{convertTemp($forecast.main.temp_max)}°</span>
                    </p>
                    <p class="h3">
                        Low <span class="font-weight-bold">{convertTemp($forecast.main.temp_min)}°</span>
                    </p>
                </div>
            </div>
            <div class="my-4">
                <h2 class="h4 text-center font-weight-bold mb-3">Today's stats</h2>
                <div class="row row-cols-4 gap-4"/>
            </div>
            <div class="d-flex justify-content-around my-4">
                <div class="text-center">
                    <WindIcon class="display-4 mb-2"/>
                    <p class="h2 font-weight-bold">{$forecast.wind.speed.toFixed(1)}mph</p>
                    <p>Wind</p>
                </div>
                <!--            TODO: Need to explore more the api to extract this information-->
                <!--            <div class="text-center">-->
                <!--                <CloudRainIcon class="display-4 mb-2" />-->
                <!--                <p class="h2 font-weight-bold">0%</p>-->
                <!--                <p>Rain</p>-->
                <!--            </div>-->
                <div class="text-center">
                    <SunriseIcon class="display-4 mb-2"/>
                    <p class="h2 font-weight-bold">{get_time($forecast.sys.sunrise, $forecast.timezone)}</p>
                    <p>Sunrise</p>
                </div>
                <div class="text-center">
                    <SunsetIcon class="display-4 mb-2"/>
                    <p class="h2 font-weight-bold">{get_time($forecast.sys.sunset, $forecast.timezone)}</p>
                    <p>Sunset</p>
                </div>
            </div>
        {/if}
    </div>

</main>

