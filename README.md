![Logo](https://github.com/doabayomi/minita_currency_exchange/blob/main/screenshot.png?raw=true)

# Minita - A Currency Exchange/Converter Platform :chart_with_upwards_trend:
## Introduction
Minita is a currency converter platform that goes beyond simple exchange rates. It provides additional insights, including sentiment analysis and relevant financial news, helping users understand factors that may influence currency value changes.


## Goal
The goal of this project is to help users make informed decisions about currency exchange rates, with plans for further enhancements like additional financial statistics and extended coverage.

[Link to Blog](https://doabayomi.hashnode.dev/minita-a-currency-converter-but-better)

[Author's LinkedIn](https://www.linkedin.com/in/daniel-abayomi-86b594226/)

## Files Description
* `app.py`: The main Flask app for handling routes, caching, and calling currency-related functions.

* `currency_api.py`: API for interacting with currency rates, conversions, and historical data.

* `market_news_api.py`: Module for retrieving market news and performing sentiment analysis.

* `currency_analysis.py`: Module to compute financial statistics like volatility index for given currency pairs.

* `templates/`: HTML templates for rendering the frontend.

* `static/`: Contains CSS, JS, and images for styling and interactivity.

## Installation
To set up the Flask app locally:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/minita.git
    cd minita
    ```
2. Create a virtual environment:
    ```bash
    Copy code
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Get necessary API keys:
    * Obtain your Marketaux API key for financial news and sentiment analysis.

    * Store it in a `config.py` file (or an environment file) in the following format:
    ```python
    MARKET_AUX_API_KEY = 'your_api_key_here'
    ```
5. Run the Flask app:
    ```bash
    flask run
    ```

## Credits/Contributions
Right now, I am the sole contributor to the project, however all contributions are welcome! :blush:

If you'd like to contribute, please submit a pull request or reach out for collaboration ideas.
