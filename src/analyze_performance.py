def calculate_ipr(pressure_bottomhole, productivity_index, flow_rate):
    """
    Calculate inflow performance relationship (IPR) curve points.
    """
    max_flow_rate = pressure_bottomhole * productivity_index
    flow_steps = [i for i in range(0, int(max_flow_rate) + 1, 10)]
    pressures = [pressure_bottomhole - (q / productivity_index) for q in flow_steps]
    return flow_steps, pressures

def analyze_wells(data):
    """
    Perform IPR analysis for each well.
    """
    analysis_results = []
    for _, row in data.iterrows():
        flow_steps, pressures = calculate_ipr(
            row['pressure_bottomhole'], 
            row['productivity_index'], 
            row['flow_rate']
        )
        analysis_results.append({
            "well_name": row['well_name'],
            "flow_steps": flow_steps,
            "pressures": pressures
        })
    return analysis_results
