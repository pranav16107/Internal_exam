const API_KEY = "YOUR_API_KEY";

const getWeather = async () => {
  let city = document.getElementById("city").value;

  if (city == "") {
    alert("Enter city name");
    return;
  }

  let url = `https://api.openweathermap.org/data/2.5/forecast?q=${city},IN&appid=${API_KEY}&units=metric`;

  try {
    let response = await fetch(url);
    let data = await response.json();

    console.log(data);

    if (data.cod != "200") {
      document.getElementById("result").innerHTML =
        `<p class="text-danger">${data.message}</p>`;
      return;
    }

    document.getElementById("result").innerHTML = `<h3>${data.city.name}</h3>
             <h4>${data.list[0].main.temp} °C</h4>
             <p>${data.list[0].weather[0].description}</p>`;

    drawChart(data);
  } catch (error) {
    document.getElementById("result").innerHTML =
      `<p class="text-danger">Error connecting to weather service</p>`;
  }
};

function drawChart(data) {
  let temperature = [];
  let time = [];

  for (let i = 0; i < 8; i++) {
    temperature.push(data.list[i].main.temp);
    time.push(data.list[i].dt_txt);
  }

  new Chart(document.getElementById("chart"), {
    type: "line",

    data: {
      labels: time,

      datasets: [
        {
          label: "Temperature °C",
          data: temperature,
        },
      ],
    },
  });
}
