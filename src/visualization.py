# src/visualization.py
# This module will create cost comparison charts using matplotlib

import matplotlib.pyplot as plt

def plot_cost_comparison(cost_data):
    labels = ['On-Demand', 'Spot', 'Savings']
    values = [
        cost_data["on_demand_cost"],
        cost_data["spot_cost"],
        cost_data["savings"]
    ]

    colors = ['skyblue', 'orange', 'lightgreen']

    plt.figure(figsize=(8, 5))
    plt.bar(labels, values, color=colors)
    plt.title(f"Cost Comparison for {cost_data['instance_type']} ({cost_data['runtime_hours']} hrs)")
    plt.ylabel("Cost ($)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


# Optional test block (for direct script testing)
if __name__ == "__main__":
    test_data = {
        "instance_type": "D4_v3",
        "runtime_hours": 5,
        "on_demand_cost": 2.40,
        "spot_cost": 0.85,
        "savings": 1.55
    }
    plot_cost_comparison(test_data)
