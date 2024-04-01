<script>
    import Search from "svelte-search";
    import {get_city_weather} from "../utils";

    let value = "";
</script>

<Search bind:value on:submit={() => get_city_weather(value)} label="" placeholder="Enter city name"/>
