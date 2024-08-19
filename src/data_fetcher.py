from os import getenv
from datetime import datetime, timedelta

import yfinance as yf
from fredapi import Fred
import streamlit as st

# Fred API key from envrionment or secrets
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

fred_api_key = getattr(st.secrets, "FRED_API_KEY", None) or getenv("FRED_API_KEY")

if not fred_api_key:
    raise ValueError(
        "FRED_API_KEY not found. Please set it in your environment, .env file, or Streamlit secrets."
    )

fred = Fred(api_key=fred_api_key)


def get_risk_free_rate(maturity_years):
    series_map = {
        1 / 12: "DTB4WK",
        2 / 12: "DTB4WK",
        3 / 12: "DTB3",
        6 / 12: "DTB6",
        1: "DGS1",
        2: "DGS2",
        3: "DGS3",
        5: "DGS5",
        7: "DGS7",
        10: "DGS10",
        20: "DGS20",
        30: "DGS30",
    }

    closest_maturity = min(series_map.keys(), key=lambda x: abs(x - maturity_years))
    series_id = series_map[closest_maturity]

    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)

    data = fred.get_series(series_id, start_date, end_date)

    if not data.empty:
        return data.iloc[-1] / 100
    else:
        return 0.05  # set to 5% if data retrieval fails


def fetch_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        history = stock.history(period="1mo")

        if history.empty:
            return {
                "current_price": info.get("regularMarketPrice", 0),
                "volatility": 0,
                "dividend_yield": float(info.get("dividendYield", 0)),
                "company_name": info.get("longName", ticker),
            }

        return {
            "current_price": info.get(
                "regularMarketPrice",
                history["Close"].iloc[-1] if not history.empty else 0,
            ),
            "volatility": history["Close"].pct_change().std() * (252**0.5)
            if not history.empty
            else 0,
            "dividend_yield": float(info.get("dividendYield", 0)),
            "company_name": info.get("longName", ticker),
        }
    except Exception as e:
        print(f"Error fetching stock data: {str(e)}")
        return {
            "current_price": 0,
            "volatility": 0,
            "dividend_yield": 0,
            "company_name": ticker,
        }
