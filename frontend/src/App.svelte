<script>
    import OpenAPIClientAxios from 'openapi-client-axios';

    import {forecast, fake_data} from './store.js'

    import CloudyIcon from './components/svg/CloudyIcon.svelte';
    import CloudRainIcon from './components/svg/CloudRainIcon.svelte';
    import SunriseIcon from './components/svg/SunriseIcon.svelte';
    import SunsetIcon from './components/svg/SunsetIcon.svelte';
    import WindIcon from './components/svg/WindIcon.svelte';

    let todo;

    (async () => {
        // window.api = new OpenAPIClientAxios({definition: '/api/openapi.json'});
        // await window.api.init();
        // window.client_api = await window.api.getClient();
        // let res = await window.client_api.get_weather("orlando");
        // console.log(res);
        console.log(fake_data);
        $forecast =
            // ...res.data,
            fake_data;  // For debug

    })();

    // async function deleteTodo(id) {
    //     let res = await window.client_api.todo_delete_id(id);
    //     if (res.status === 200) {
    //         $todos = $todos.filter(item => item._id.$oid !== res.data._id.$oid);
    //         console.log($todos);
    //     } else {
    //         console.log(res);
    //     }
    // }


</script>

<main>

    <div class="text-white min-vh-100 p-5">
        <div class="text-center">
            <h1 class="display-4 font-weight-bold">London, UK</h1>
            <p class="h2">Sunday 4th August</p>
        </div>
        <div class="d-flex justify-content-center align-items-center my-4">
            <CloudyIcon class="text-primary" />
            <span class="font-weight-bold display-1">21°</span>
            <div class="text-right">
                <p class="h4 font-weight-bold">Mostly Sunny</p>
                <p class="h2">
                    High <span class="font-weight-bold">23°</span>
                </p>
                <p class="h2">
                    Low <span class="font-weight-bold">14°</span>
                </p>
            </div>
        </div>
        <div class="my-4">
            <h2 class="h4 text-center font-weight-bold mb-3">Today's stats</h2>
            <div class="row row-cols-4 gap-4" />
        </div>
        <div class="d-flex justify-content-around my-4">
            <div class="text-center">
                <WindIcon class="display-4 mb-2" />
                <p class="h2 font-weight-bold">7mph</p>
                <p>Wind</p>
            </div>
            <div class="text-center">
                <CloudRainIcon class="display-4 mb-2" />
                <p class="h2 font-weight-bold">0%</p>
                <p>Rain</p>
            </div>
            <div class="text-center">
                <SunriseIcon class="display-4 mb-2" />
                <p class="h2 font-weight-bold">05:27</p>
                <p>Sunrise</p>
            </div>
            <div class="text-center">
                <SunsetIcon class="display-4 mb-2" />
                <p class="h2 font-weight-bold">20:57</p>
                <p>Sunset</p>
            </div>
        </div>
    </div>

</main>


<!--<style>-->

<!--    .row {-->
<!--        padding-top: 1rem;-->
<!--        display: flex;-->
<!--        justify-content: space-evenly;-->
<!--    }-->

<!--    #profile {-->
<!--        margin-right: -20px;-->
<!--        border-radius: 50%;-->
<!--        box-shadow: 3px 3px 20px rgba(0, 0, 0, 0.5);-->
<!--        border: 2px solid rgba(255, 255, 255, 1);-->
<!--    }-->

<!--    .bottom {-->
<!--        position: absolute;-->
<!--        bottom: 1%;-->
<!--        left: 50%;-->
<!--        -webkit-transform: translate(-50%, 0%);-->
<!--        transform: translate(-50%, 0%);-->
<!--    }-->

<!--    .custom-btn {-->
<!--        margin-top: 10px;-->
<!--        margin-left: 10px;-->
<!--    }-->

<!--</style>-->
