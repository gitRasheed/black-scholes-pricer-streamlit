import pytest
import numpy as np
from visualizations import create_heatmap, create_profit_loss_chart, create_greeks_plot

def test_create_heatmap():
    S_range = np.linspace(90, 110, 10)
    sigma_range = np.linspace(0.1, 0.3, 10)
    pnl = np.random.randn(10, 10)
    option_prices = np.random.randn(10, 10)
    fig = create_heatmap(S_range, sigma_range, pnl, option_prices, "Test Heatmap")
    assert fig.layout.title.text == "Test Heatmap"
    assert fig.layout.xaxis.title.text == "Stock Price"
    assert fig.layout.yaxis.title.text == "Volatility"

def test_create_profit_loss_chart():
    S_range = np.linspace(90, 110, 10)
    pnl = np.random.randn(10)
    break_even = 100
    fig = create_profit_loss_chart(S_range, pnl, break_even, "Test P&L Chart")
    assert fig.layout.title.text == "Test P&L Chart"
    assert fig.layout.xaxis.title.text == "Stock Price"
    assert fig.layout.yaxis.title.text == "Profit/Loss"
    assert len(fig.data) == 4  # Main line, break-even point, profit area, loss area

def test_create_greeks_plot():
    S_range = np.linspace(90, 110, 10)
    greeks = {
        "delta_call": np.random.rand(10),
        "gamma": np.random.rand(10),
        "vega": np.random.rand(10),
        "theta_call": np.random.rand(10),
        "rho_call": np.random.rand(10)
    }
    fig = create_greeks_plot(S_range, greeks, "Test Greeks Plot")
    assert fig.layout.title.text == "Test Greeks Plot"
    assert fig.layout.xaxis.title.text == "Stock Price"
    assert fig.layout.yaxis.title.text == "Greek Value"
    assert len(fig.data) == 5  # One line for each Greek