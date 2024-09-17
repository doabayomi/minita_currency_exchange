// Getting currency exchange parameters
const currentURL = window.location.search
const fieldsInURL = new URLSearchParams(currentURL)
const currencyFrom = fieldsInURL.get("from")
const currencyTo = fieldsInURL.get("to")

// Creating the chart object
ctx = document.getElementById("price-chart")
const priceChart = new Chart(ctx, {
    type: "line",
    data: {
        labels: [],
        datasets: [{
            label: `${currencyFrom.toUpperCase()} to ${currencyTo.toUpperCase()} rate`,
            data: [],
            tension: 0.1,
            borderColor: '#596f62',
            fill: false
        }]
    },
    options: {
        scales: {
            x: {
                grid: {
                    display: false
                },
                display: false
            },
            y: {
                beginAtZero: false
            }
        },
        plugins: {
            legend: {
                display: false
            }
        }
    }
})

function updateChart(timeframe){
    // Setting up a loading state
    const loadingText = document.getElementById("price-chart__loading-text")
    const chartContainer = document.querySelector("#price-chart__container")
    loadingText.style.display = 'block'
    chartContainer.style.opacity = '0.5'

    // Fetching rates data from api based on timeframe
    fetch(`/api/prices/${timeframe}/${currencyFrom}/${currencyTo}`)
    .then(response => response.json())
    .then(data => {
        priceChart.data.labels = Object.keys(data)
        priceChart.data.datasets[0].data = Object.values(data)
        priceChart.update()

        // Go back to original state from loading state
        loadingText.style.display = 'none';
        chartContainer.style.opacity = '1';
    })
    .catch(error => {
        console.error('Error fetching chart data: ', error);
        loadingText.textContent = 'Failed to load data'
    })
}

updateChart('weekly')

// Getting all timestamp tabs
const timeframes = document.querySelectorAll(".timestamp-tab")
timeframes.forEach(option => {
    option.addEventListener('click', function() {
        // removing selected tag from all timestamp-tabs
        timeframes.forEach(opt => {
            opt.classList.remove('selected')
        })

        this.classList.add('selected')
        // Accessing timeframe variable
        updateChart(this.dataset.timeframe);
    })
})