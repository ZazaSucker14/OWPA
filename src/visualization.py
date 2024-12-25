import matplotlib.pyplot as plt

def visualize_ipr(analysis_results):
    """
    Visualize IPR curves for multiple wells.
    """
    plt.figure(figsize=(10, 6))
    for result in analysis_results:
        plt.plot(result["flow_steps"], result["pressures"], label=result["well_name"])
    plt.title("Inflow Performance Relationship (IPR) Curves")
    plt.xlabel("Flow Rate (STB/day)")
    plt.ylabel("Bottomhole Pressure (psi)")
    plt.legend()
    plt.grid(True)
    plt.show()
    
def visualize_lift_efficiency(data):
    """
    Visualize lift efficiency for all wells.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(data['well_name'], data['lift_efficiency'], color='orange')
    plt.title("Lift Efficiency for Wells")
    plt.xlabel("Well Name")
    plt.ylabel("Efficiency")
    plt.grid(axis='y')
    plt.show()

def visualize_production_forecast(forecasts):
    """
    Visualize production forecast for all wells.
    """
    plt.figure(figsize=(12, 8))
    for well, forecast in forecasts.items():
        plt.plot(forecast['time'], forecast['rates'], label=well)
    plt.title("Production Forecast")
    plt.xlabel("Time (months)")
    plt.ylabel("Production Rate (STB/day)")
    plt.legend()
    plt.grid(True)
    plt.show()
