
import numpy as np
from scipy.stats import norm

def black_scholes(S, X, T, r, sigma, option_type="call"):
    """
    Calculate the Black-Scholes option price.
    
    Parameters:
    S : float
        Current stock price
    X : float
        Option strike price
    T : float
        Time to expiration in years
    r : float
        Risk-free interest rate (annual)
    sigma : float
        Volatility of the stock (annual)
    option_type : str
        "call" for call option price, "put" for put option price
    
    Returns:
    float
        Option price based on Black-Scholes model
    """
    d1 = (np.log(S / X) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == "call":
        option_price = S * norm.cdf(d1) - X * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        option_price = X * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")
    
    return option_price

# Example usage:
S = 100  # Current stock price
X = 100  # Strike price
T = 1    # Time to expiration (1 year)
r = 0.05 # Risk-free interest rate (5%)
sigma = 0.2 # Volatility (20%)

call_price = black_scholes(S, X, T, r, sigma, option_type="call")
put_price = black_scholes(S, X, T, r, sigma, option_type="put")

print(f"Call Option Price: {call_price:.2f}")
print(f"Put Option Price: {put_price:.2f}")

#%%
