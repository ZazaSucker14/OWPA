def calculate_lift_efficiency(power_input, fluid_production, pump_efficiency=0.8):
    """
    Calculate artificial lift efficiency.
    """
    try:
        efficiency = (fluid_production * pump_efficiency) / power_input
        return efficiency
    except ZeroDivisionError:
        print("Error: Power input cannot be zero.")
        return None

def analyze_lift_efficiency(data):
    """
    Add lift efficiency analysis for each well.
    """
    lift_efficiencies = []
    for _, row in data.iterrows():
        efficiency = calculate_lift_efficiency(
            power_input=row['power_input'],
            fluid_production=row['flow_rate']
        )
        lift_efficiencies.append(efficiency)
    data['lift_efficiency'] = lift_efficiencies
    return data
