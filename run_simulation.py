# run_simulation.py

import argparse
from src.spark_simulator import run_word_count, run_aggregation_job
from src.cost_calculator import calculate_cost
from src.visualization import plot_cost_comparison

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--job", choices=["wordcount", "aggregation"], required=True)
    parser.add_argument("--instance_type", required=True)
    parser.add_argument("--runtime_hours", type=float, required=True)
    parser.add_argument("--save_plot", action="store_true")
    args = parser.parse_args()

    # Run Spark Job
    if args.job == "wordcount":
        run_word_count()
    elif args.job == "aggregation":
        run_aggregation_job()

    # Calculate cost
    cost_data = calculate_cost(args.instance_type, args.runtime_hours)

    # Visualize
    if cost_data:
        plot_cost_comparison(
            cost_data,
            save_path="artifacts/plot.png" if args.save_plot else None
        )

if __name__ == "__main__":
    main()