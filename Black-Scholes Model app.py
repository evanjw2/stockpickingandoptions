import numpy as np
from scipy.stats import norm
import tkinter as tk
from tkinter import messagebox

def black_scholes(S, X, T, r, sigma, option_type="call"):
    d1 = (np.log(S / X) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == "call":
        option_price = S * norm.cdf(d1) - X * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        option_price = X * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")
    
    return option_price

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

def calculate():
    try:
        S = float(entry_S.get())
        X = float(entry_X.get())
        T = float(entry_T.get())
        r = float(entry_r.get())
        sigma = float(entry_sigma.get())
        option_type = var_option_type.get()
        
        price = black_scholes(S, X, T, r, sigma, option_type)
        
        messagebox.showinfo("Result", f"{option_type.capitalize()} Option Price: {price:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")

# Create the main window
root = tk.Tk()
root.title("Black-Scholes Option Calculator")

# Labels and entries for inputs
tk.Label(root, text="Stock Price (S)").grid(row=0, column=0)
entry_S = tk.Entry(root)
entry_S.grid(row=0, column=1)

tk.Label(root, text="Strike Price (X)").grid(row=1, column=0)
entry_X = tk.Entry(root)
entry_X.grid(row=1, column=1)

tk.Label(root, text="Time to Expiration (T)").grid(row=2, column=0)
entry_T = tk.Entry(root)
entry_T.grid(row=2, column=1)

tk.Label(root, text="Risk-Free Rate (r)").grid(row=3, column=0)
entry_r = tk.Entry(root)
entry_r.grid(row=3, column=1)

tk.Label(root, text="Volatility (σ)").grid(row=4, column=0)
entry_sigma = tk.Entry(root)
entry_sigma.grid(row=4, column=1)

# Option type selection
var_option_type = tk.StringVar(value="call")
tk.Label(root, text="Option Type").grid(row=5, column=0)
tk.Radiobutton(root, text="Call", variable=var_option_type, value="call").grid(row=5, column=1)
tk.Radiobutton(root, text="Put", variable=var_option_type, value="put").grid(row=5, column=2)

# Calculate button
tk.Button(root, text="Calculate", command=calculate).grid(row=6, column=0, columnspan=3)

# Run the application
root.mainloop()
