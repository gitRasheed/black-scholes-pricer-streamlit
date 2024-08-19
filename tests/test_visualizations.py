import numpy as np
import pytest

from src.visualizations import (
    create_greeks_plot,
    create_heatmap,
    create_profit_loss_chart,
)


@pytest.fixture
def stock_range():
    return np.linspace(90, 110, 10)


@pytest.fixture
def volatility_range():
    return np.linspace(0.1, 0.3, 10)


@pytest.fixture
def random_2d_data():
    return np.random.randn(10, 10)


@pytest.fixture
def random_1d_data():
    return np.random.randn(10)


@pytest.fixture
def greek_data():
    return {
        "delta_call": np.random.rand(10),
        "gamma": np.random.rand(10),
        "vega": np.random.rand(10),
        "theta_call": np.random.rand(10),
        "rho_call": np.random.rand(10),
    }


def test_create_heatmap(stock_range, volatility_range, random_2d_data):
    fig = create_heatmap(stock_range, volatility_range, random_2d_data, random_2d_data, "Test Heatmap")

    assert fig.layout.title.text == "Test Heatmap"
    assert fig.layout.xaxis.title.text == "Stock Price"
    assert fig.layout.yaxis.title.text == "Volatility"

    assert fig.data[0].type == "heatmap"
    assert np.array_equal(fig.data[0].x, stock_range)
    assert np.array_equal(fig.data[0].y, volatility_range)


def test_create_profit_loss_chart(stock_range, random_1d_data):
    break_even = 100
    fig = create_profit_loss_chart(stock_range, random_1d_data, break_even, "Test P&L Chart")

    assert fig.layout.title.text == "Test P&L Chart"
    assert fig.layout.xaxis.title.text == "Stock Price"
    assert fig.layout.yaxis.title.text == "Profit/Loss"

    assert len(fig.data) == 4
    assert fig.data[0].name == "P&L"
    assert fig.data[1].name == "Break-even"
    assert fig.data[2].name == "Profit"
    assert fig.data[3].name == "Loss"


@pytest.mark.parametrize("expected_greek_count", [5])
def test_create_greeks_plot(stock_range, greek_data, expected_greek_count):
    fig = create_greeks_plot(stock_range, greek_data, "Test Greeks Plot")

    assert fig.layout.title.text == "Test Greeks Plot"
    assert fig.layout.xaxis.title.text == "Stock Price"
    assert fig.layout.yaxis.title.text == "Greek Value"

    assert len(fig.data) == expected_greek_count

    expected_names = ["Delta", "Gamma", "Vega", "Theta", "Rho"]
    for i, name in enumerate(expected_names):
        assert fig.data[i].name == name
        assert np.array_equal(fig.data[i].x, stock_range)
