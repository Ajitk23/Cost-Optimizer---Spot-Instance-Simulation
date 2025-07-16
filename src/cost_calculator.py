# This module will calculate cost based on job metrics and pricing data

import json

def calculate_cost(instance_type, runtime_hours):

    with open("data/pricing.json") as p:
        pricing = json.load(p)

    if instance_type not in pricing:
        print(f"Instance type '{instance_type}' not found in pricing.json!")
        return
    
    onDemandRate = pricing[instance_type]["on_demand"]
    spotRate = pricing[instance_type]["spot"]

    # calculate costs
    onDemandCost = runtime_hours * onDemandRate
    spotCost = runtime_hours * spotRate 
    savings = onDemandCost - spotCost

    print(f"\n Cost Summary for instance type '{instance_type}': ")
    print(f" Runtime (hours): {runtime_hours}")
    print(f" On-Demand cost: ${onDemandCost:.2f}")
    print(f" Spot cost: ${spotCost:.2f}")
    print(f" Estimated savings: ${savings:.2f}\n")

    return {
        "instance_type": instance_type,
        "runtime_hours": runtime_hours,
        "on_demand_cost": onDemandCost,
        "spot_cost": spotCost,
        "savings": savings
    }

if __name__ == "__main__":

    calculate_cost("D4_v3", 5)