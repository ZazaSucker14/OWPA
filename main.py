from matplotlib import pyplot as plt
from src.input_data import load_well_data
from src.analyze_performance import analyze_wells
from src.visualization import visualize_ipr, visualize_lift_efficiency, visualize_production_forecast
from src.export_data import export_analysis_to_csv
from src.lift_efficiency import analyze_lift_efficiency
from src.production_forecast import generate_forecast

def main():
    # Step 1: Load well data
    file_path = "data/well_data.csv"
    data = load_well_data(file_path)
    if data is None:
        return

    # Step 2: Analyze well performance
    analysis_results = analyze_wells(data)

    # Step 3: Analyze lift efficiency
    data = analyze_lift_efficiency(data)

    # Step 4: Generate production forecast
    time_period = 12  # Forecast for 12 months
    forecasts = generate_forecast(data, time_period)

    # Step 5: Visualize results
    visualize_ipr(analysis_results)
    visualize_lift_efficiency(data)
    visualize_production_forecast(forecasts)

    # Show all plots at once
    plt.show()

    # Step 6: Export results
    output_path = "data/analysis_results.csv"
    export_analysis_to_csv(data, output_path)

if __name__ == "__main__":
    main()
