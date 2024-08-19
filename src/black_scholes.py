import numpy as np
from scipy.stats import norm


class BlackScholes:
    def __init__(self, s, k, t, r, sigma, q=0.0):
        self.s, self.k, self.t, self.r, self.sigma, self.q = s, k, t, r, sigma, q

    def calculate_option_price(self, option_type="call"):
        d1 = (np.log(self.s / self.k) + (self.r - self.q + 0.5 * self.sigma**2) * self.t) / (
            self.sigma * np.sqrt(self.t)
        )
        d2 = d1 - self.sigma * np.sqrt(self.t)

        if option_type == "call":
            price = self.s * np.exp(-self.q * self.t) * norm.cdf(d1) - self.k * np.exp(-self.r * self.t) * norm.cdf(d2)
        else:
            price = self.k * np.exp(-self.r * self.t) * norm.cdf(-d2) - self.s * np.exp(-self.q * self.t) * norm.cdf(
                -d1
            )

        return price

    def calculate_greeks(self):
        d1 = (np.log(self.s / self.k) + (self.r - self.q + 0.5 * self.sigma**2) * self.t) / (
            self.sigma * np.sqrt(self.t)
        )
        d2 = d1 - self.sigma * np.sqrt(self.t)

        greeks = {
            "delta_call": np.exp(-self.q * self.t) * norm.cdf(d1),
            "delta_put": -np.exp(-self.q * self.t) * norm.cdf(-d1),
            "gamma": np.exp(-self.q * self.t) * norm.pdf(d1) / (self.s * self.sigma * np.sqrt(self.t)),
            "vega": self.s * np.exp(-self.q * self.t) * norm.pdf(d1) * np.sqrt(self.t),
            "theta_call": -self.s * np.exp(-self.q * self.t) * norm.pdf(d1) * self.sigma / (2 * np.sqrt(self.t))
            - self.r * self.k * np.exp(-self.r * self.t) * norm.cdf(d2)
            + self.q * self.s * np.exp(-self.q * self.t) * norm.cdf(d1),
            "theta_put": -self.s * np.exp(-self.q * self.t) * norm.pdf(d1) * self.sigma / (2 * np.sqrt(self.t))
            + self.r * self.k * np.exp(-self.r * self.t) * norm.cdf(-d2)
            - self.q * self.s * np.exp(-self.q * self.t) * norm.cdf(-d1),
            "rho_call": self.k * self.t * np.exp(-self.r * self.t) * norm.cdf(d2),
            "rho_put": -self.k * self.t * np.exp(-self.r * self.t) * norm.cdf(-d2),
        }
        return greeks

    def calculate_profit_loss(self, option_type, purchase_price, current_stock_price):
        if option_type == "call":
            pnl = max(current_stock_price - self.k, 0) - purchase_price
        else:
            pnl = max(self.k - current_stock_price, 0) - purchase_price
        return pnl
