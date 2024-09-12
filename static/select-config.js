document.addEventListener('DOMContentLoaded', function() {
    // Initialize SlimSelect on the select elements
    new SlimSelect({
        select: "#currency-from"
    })

    new SlimSelect({
        select: "#currency-to"
    })

    // Set default values for the select elements
    const selectDefault = () => {
        const fromSelect = document.querySelector("#currency-from")
        const toSelect = document.querySelector("#currency-to")
        
        if (fromSelect && toSelect) {
            fromSelect.value = "usd"
            toSelect.value = "eur"
        }
    };

    selectDefault()
})
