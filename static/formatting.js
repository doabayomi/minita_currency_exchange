/* getting the news section dates and changing it from a timestamp
to the format {Month dd, yyyy}
*/
const timestampElements = document.querySelectorAll(".news-date")
timestampElements.forEach(element => {
    const timestamp = element.textContent.trim();
    const date = new Date(timestamp)
    
    const dateOptions = {year: 'numeric', month: 'long', day: 'numeric'}
    const formattedDate = date.toLocaleDateString('en-US', dateOptions)

    element.textContent = formattedDate;
})


// Format numbers by adding comma's in JS
const baseCurrencyValue = document.querySelector("#base-amount")
const targetCurrencyValue = document.querySelector("#converted-amount")

const formattedBaseValue = Number(baseCurrencyValue.textContent.trim()).toLocaleString()
const formatttedConvertedValue = Number(targetCurrencyValue.textContent.trim()).toLocaleString()

baseCurrencyValue.textContent = formattedBaseValue
targetCurrencyValue.textContent = formatttedConvertedValue


// Color coding sentiment scores and arrows and calculating final score
sentimentScores = document.querySelectorAll('.news__sentiment-score')
finalScoreElement = document.querySelector("#final-sentiment-score")
if (sentimentScores.length > 0) {
    count = 0;
    scoresTotal = 0;
    sentimentScores.forEach(element => {
        const arrow = element.children[0]
        const valueElement = element.children[1]
        const value  = parseFloat(valueElement.textContent.trim())
    
        if (value > 0) {
            arrow.classList.add('up')
            valueElement.classList.add('state-good')
        } else {
            arrow.classList.add('down')
            valueElement.classList.add('state-bad')
        }
        scoresTotal += value
        count++
    })
    finalScoreElement.textContent = (scoresTotal / count).toFixed(5)
    if (parseFloat(finalScoreElement.textContent.trim()) > 0) {
        finalScoreElement.classList.add('state-good')
    } else {
        finalScoreElement.classList.add('state-bad')
    }
} else {
    finalScoreElement.textContent = 'N/A'
}

// Color coding volatility indexes
volatilityIndexElements = document.querySelectorAll('.volatility')
volatilityIndexElements.forEach(element => {
    value = parseFloat(element.textContent.trim())
    if (value < 0.001) {
        element.classList.add('state-good')
    } else if (value >= 0.001 && value <= 0.005) {
        element.classList.add('state-neutral')
    } else {
        element.classList.add('state-bad')
    }
})
