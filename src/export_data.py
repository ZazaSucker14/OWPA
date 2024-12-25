import pandas as pd

def export_analysis_to_csv(analysis_results, output_path):
    """
    Export analysis results to a CSV file.
    """
    flat_data = []
    for result in analysis_results:
        for flow, pressure in zip(result["flow_steps"], result["pressures"]):
            flat_data.append({
                "well_name": result["well_name"],
                "flow_rate": flow,
                "bottomhole_pressure": pressure
            })
    df = pd.DataFrame(flat_data)
    df.to_csv(output_path, index=False)
    print(f"Results exported to {output_path}")
