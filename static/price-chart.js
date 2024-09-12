const currentURL = window.location.search
const fieldsInURL = new URLSearchParams(currentURL)
const currencyFrom = fieldsInURL.get("from")
const currencyTo = fieldsInURL.get("to")

ctx = document.getElementById("price-chart")

const priceChart = new Chart(ctx, {
    type: "line",
    data: {
        labels: [],
        datasets: [{
            label: `${currencyFrom.toUpperCase()} to ${currencyTo.toUpperCase()} rate`,
            data: [],
            fill: true,
            tension: 0.2
            // borderColor: to be decided based on theme
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: false
            }
        }
    }
})

function updateChart(timeframe){
    fetch(`/api/prices/${timeframe}/${currencyFrom}/${currencyTo}`)
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