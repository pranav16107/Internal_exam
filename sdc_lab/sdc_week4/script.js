async function getWeather() {
    let city = document.getElementById("city").value.trim();

    if (city == "") {
        alert("Enter a city name");
        return;
    }

    let key = "b19d6dbc4fc7ed53c9f63a2b287867c2";
    let url = `https://api.openweathermap.org/data/2.5/weather?q=${encodeURIComponent(city)}&units=metric&appid=${key}`;

    try {
        let response = await fetch(url);
        let data = await response.json();

        if (!response.ok) {
            throw new Error(data.message);
        }

        document.getElementById("result").innerHTML =
            "City: " + data.name +
            "<br>Temperature: " + data.main.temp + " °C";

    } catch (error) {
        document.getElementById("result").innerHTML =
            "Error: " + error.message;
    }
}