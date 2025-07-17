# 💸 Cost Optimizer - Spot Instance Simulation

A mini cloud cost-optimization simulator that demonstrates the **cost difference between On-Demand and Spot Instances** using Spark jobs on simulated workloads (like Word Count or Aggregation). Also visualizes estimated savings with clear matplotlib charts.

---

## 🚀 Features

- 🧠 Simulates real Spark jobs: Word Count and Aggregation
- 💸 Calculates cost for On-Demand vs Spot instance types
- 📊 Visualizes savings using bar charts
- 📁 Organized modular codebase with CLI support
- ✅ Clean Python 3.11 and PySpark-based implementation

---

## 🧱 Folder Structure

Cost-Optimizer---Spot-Instance-Simulation/
├── data/
│ ├── sample_wordcount.csv
│ └── sample_aggregation.csv
│
├── artifacts/ # Generated charts
│ └── wordcount_cost_comparison.png
│
├── notebooks/
│ └── main_simulation_notebook.ipynb
│
├── src/
│ ├── init.py
│ ├── spark_simulator.py # Spark job logic
│ ├── cost_calculator.py # Cost calculations
│ └── visualization.py # Bar chart generator
│
├── run_simulation.py # ✅ Main CLI entry point
├── requirements.txt
├── README.md
└── .gitignore


---

## ⚙️ Setup Instructions

### ✅ 1. Clone the repository

```bash
git clone https://github.com/Ajitk23/Cost-Optimizer---Spot-Instance-Simulation.git
cd Cost-Optimizer---Spot-Instance-Simulation

✅ 2. Create a virtual environment
create -p venv python=3.11 -y
conda activate ./venv

✅ 3. Install dependencies
pip install -r requirements.txt

▶ How to Run

🟡 Word Count Simulation
python run_simulation.py --job wordcount --instance_type D4_v3 --runtime_hours 5 --save_plot

🔵 Aggregation Simulation
python run_simulation.py --job aggregation --instance_type D4_v3 --runtime_hours 3 --save_plot
Use --save_plot to save the chart to artifacts/

📊 Output Sample
You’ll see bar charts comparing:

On-Demand cost

Spot cost

💰 Estimated savings
Image gets saved in artifacts/ folder like:

bash
Copy
Edit
artifacts/wordcount_cost_comparison.png

📦 Requirements
Sample requirements.txt (you can generate using pip freeze > requirements.txt):
txt
Copy
Edit
matplotlib
pyspark

🧪 Coming Soon
Export word count / aggregation result to CSV

Add more realistic pricing data

Option to simulate longer job pipelines

Author
Ajit Kumar
Project under internship initiative.
GitHub: Ajitk23