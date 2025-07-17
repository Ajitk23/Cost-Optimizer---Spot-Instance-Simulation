# visualization.py
# Thi smodule will create cost comparision charts using matplotlib

import matplotlib.pyplot as plt


def plot_cost_comparision(cost_data):

    labels = ['onDemand', 'spot', 'savings']
    values = [
        cost_data["onDemandCost"],
        cost_data["spotCost"],
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



