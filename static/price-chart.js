currencyFrom = document.querySelector("#currency-from").value
currencyTo = document.querySelector("#currency_to").value
ctx = document.getElementById("price-chart")

const priceChart = new Chart(ctx, {
    type: "line",
    data: {
        labels: [],
        datasets: [{
            label: `${currencyFrom} to ${currencyTo} rate`,
            data: [],
            tension: 0.2
            // borderColor: to be decided based on theme
        }]
    },
    options: {
        scales: {
            x: {
                type: "time",
                time: {
                    unit: "day"
                }
            },
            y: {
                beginAtZero: false
            }
        }
    }
})

function updateChart(timeframe){
    fetch(`/api/currency/${timeframe}/${currency_from}/${currency_to}`)
    .then(response => response.json())
    .then(data => {
        priceChart.data.labels = Object.keys(data);
        priceChart.data.datasets[0].data = Object.values(data);
        priceChart.update();
    });
}

document.getElementById('timeframe-weekly').addEventListener('click', () => updateChart('weekly'));
document.getElementById('timeframe-monthly').addEventListener('click', () => updateChart('monthly'));
document.getElementById('timeframe-yearly').addEventListener('click', () => updateChart('yearly'));

updateChart('weekly');