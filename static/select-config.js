document.addEventListener('DOMContentLoaded', function() {
    // Initialize SlimSelect on the select elements
    var fromSelect = new SlimSelect({
        select: "#currency-from",
        settings: {
            showOptionTooltips: true
        }
    })

    var toSelect = new SlimSelect({
        select: "#currency-to"
    })

    fromSelect.setSelected("usd")
    toSelect.setSelected("eur")

})
