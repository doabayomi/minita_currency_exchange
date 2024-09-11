const chart_data_path = "/static/data/chart.json"
fetch(chart_data_path)
    .then((response) => {
        if (!response.ok) {
            throw new Error('Failed to load JSON data')
        }
        return response.json()
    })
    .then((price_data) => {
        const labels = price_data.dates
        const base_currency = price_data.base_currency_prices
        const target_currency = price_data.target_currency_prices
        console.log(base_currency)
        console.log(target_currency)

        const ctx = document.getElementById('price-chart')
        const usdChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: price_data.currency_names[0],
                    data: base_currency,
                    fill: false,
                    tension: 0.1
                },{
                    label: price_data.currency_names[1],
                    data: target_currency,
                    fill: false,
                    tension: 0.1
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
    })