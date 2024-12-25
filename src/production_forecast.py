import numpy as np

def forecast_production(initial_rate, decline_rate, time, model='exponential'):
    """
    Forecast production rate using decline curve analysis.
    """
    if model == 'exponential':
        return initial_rate * np.exp(-decline_rate * time)
    elif model == 'hyperbolic':
        b = 0.5  # Default hyperbolic exponent
        return initial_rate / ((1 + b * decline_rate * time) ** (1 / b))
    else:
        print("Error: Unsupported model. Choose 'exponential' or 'hyperbolic'.")
        return None

def generate_forecast(data, time_period):
    """
    Generate production forecast for each well over a specified time period.
    """
    forecasts = {}
    for _, row in data.iterrows():
        time = np.arange(0, time_period + 1, 1)  # Time steps (e.g., months)
        rates = forecast_production(row['flow_rate'], decline_rate=0.1, time=time)
        forecasts[row['well_name']] = {"time": time, "rates": rates}
    return forecasts
