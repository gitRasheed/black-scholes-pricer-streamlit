import pytest
from black_scholes import BlackScholes

@pytest.fixture
def bs_instance():
    return BlackScholes(S=100, K=100, T=1, r=0.05, sigma=0.2, q=0.01)

def test_call_option_price(bs_instance):
    call_price = bs_instance.calculate_option_price("call")
    assert 8 < call_price < 15, f"Call price {call_price} is out of expected range"

def test_put_option_price(bs_instance):
    put_price = bs_instance.calculate_option_price("put")
    assert 5 < put_price < 12, f"Put price {put_price} is out of expected range"

def test_greeks(bs_instance):
    greeks = bs_instance.calculate_greeks()
    assert 0.5 < greeks['delta_call'] < 0.7, "Delta of ATM call should be close to 0.5"
    assert -0.7 < greeks['delta_put'] < -0.3, "Delta of ATM put should be close to -0.5"
    assert greeks['gamma'] > 0, "Gamma should be positive"
    assert greeks['vega'] > 0, "Vega should be positive"
    assert greeks['theta_call'] < 0, "Theta of call should be negative"
    assert greeks['theta_put'] < 0, "Theta of put should be negative"

def test_profit_loss(bs_instance):
    call_pnl = bs_instance.calculate_profit_loss("call", 10, 110)
    put_pnl = bs_instance.calculate_profit_loss("put", 10, 90)
    assert call_pnl == 0, "Call PnL should be 0 when stock price equals strike plus premium"
    assert put_pnl == 0, "Put PnL should be 0 when stock price equals strike minus premium"