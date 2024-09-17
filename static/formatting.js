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


// Color coding sentiment scores and arrows
sentimentScores = document.querySelectorAll('.news__sentiment-score')
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
})
