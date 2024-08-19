## Project Overview

Black-Scholes option pricer in streamlit with customizable parameters, ability to use real market data, and visualizations for PnL & Greeks in reaction to different volatilities and prices. Also used this as an opportunity to test a basic pipeline with GitHub Actions & implement Ruff linting & formatting within it.

## Features

- Real-time stock data fetching using yfinance
- Dynamic risk-free rate retrieval from FRED (based off the closest treasury to the option maturity time)
- Interactive option pricing for both calls and puts
- Visualization of option Greeks (Delta, Gamma, Vega, Theta, Rho)
- Heat maps for option price and PnL across different stock prices and volatilities
- Profit/Loss charts for visual analysis of option strategies

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/black-scholes-option-pricer.git
   cd black-scholes-option-pricer
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your FRED API key:
   - Obtain a FRED API key from [https://fred.stlouisfed.org/docs/api/api_key.html](https://fred.stlouisfed.org/docs/api/api_key.html)
   - Set the API key as an environment variable named `FRED_API_KEY`

## Usage

Run the Streamlit app:
```
streamlit run app.py
```

Navigate to the provided local URL in your web browser to use the application.

## Project Structure

- `app.py`: Main Streamlit application
- `src/`:
  - `black_scholes.py`: Black-Scholes model implementation
  - `data_fetcher.py`: Functions for fetching stock and economic data
  - `visualizations.py`: Functions for creating interactive plots
- `requirements.txt`: List of Python dependencies

## Technologies Used

- Python
- Streamlit
- NumPy
- Pandas
- Plotly
- yfinance
- FRED API
