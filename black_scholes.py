import numpy as np
from scipy.stats import norm

class BlackScholes:
    def __init__(self, S, K, T, r, sigma, q=0):
        self.S, self.K, self.T, self.r, self.sigma, self.q = S, K, T, r, sigma, q

    def calculate_option_price(self, option_type='call'):
        d1 = (np.log(self.S / self.K) + (self.r - self.q + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * np.sqrt(self.T))
        d2 = d1 - self.sigma * np.sqrt(self.T)

        if option_type == 'call':
            price = self.S * np.exp(-self.q * self.T) * norm.cdf(d1) - self.K * np.exp(-self.r * self.T) * norm.cdf(d2)
        else:
            price = self.K * np.exp(-self.r * self.T) * norm.cdf(-d2) - self.S * np.exp(-self.q * self.T) * norm.cdf(-d1)

        return price

    def calculate_greeks(self):
        d1 = (np.log(self.S / self.K) + (self.r - self.q + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * np.sqrt(self.T))
        d2 = d1 - self.sigma * np.sqrt(self.T)

        greeks = {
            'delta_call': np.exp(-self.q * self.T) * norm.cdf(d1),
            'delta_put': -np.exp(-self.q * self.T) * norm.cdf(-d1),
            'gamma': np.exp(-self.q * self.T) * norm.pdf(d1) / (self.S * self.sigma * np.sqrt(self.T)),
            'vega': self.S * np.exp(-self.q * self.T) * norm.pdf(d1) * np.sqrt(self.T),
            'theta_call': -self.S * np.exp(-self.q * self.T) * norm.pdf(d1) * self.sigma / (2 * np.sqrt(self.T)) 
                          - self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(d2) 
                          + self.q * self.S * np.exp(-self.q * self.T) * norm.cdf(d1),
            'theta_put': -self.S * np.exp(-self.q * self.T) * norm.pdf(d1) * self.sigma / (2 * np.sqrt(self.T)) 
                         + self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(-d2) 
                         - self.q * self.S * np.exp(-self.q * self.T) * norm.cdf(-d1),
            'rho_call': self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(d2),
            'rho_put': -self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(-d2)
        }
        return greeks

    def calculate_profit_loss(self, option_type, purchase_price, current_stock_price):
        current_option_price = self.calculate_option_price(option_type)
        if option_type == 'call':
            pnl = max(current_stock_price - self.K, 0) - purchase_price
        else:
            pnl = max(self.K - current_stock_price, 0) - purchase_price
        return pnl