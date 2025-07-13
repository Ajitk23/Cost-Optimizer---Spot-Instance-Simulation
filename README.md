# Cost Optimizer – Spot Instance Simulation

## 📌 Project Overview

This project is an **educational Databricks notebook** that **simulates and visualizes cost savings** when running sample Spark jobs on **spot instances** versus **on-demand instances** in the cloud.

It helps **students, data engineers, and analysts** learn **how to reduce cloud computing costs** by understanding the pricing difference between spot and on-demand compute resources.

---

## 🎯 Business Requirement

Cloud providers like AWS, Azure, and GCP offer **spot instances** (unused compute capacity sold at a discount) and **on-demand instances** (always available but more expensive).  
Running big data jobs on spot instances can save significant money — but comes with trade-offs like possible interruption.

This notebook shows how:
- The same Spark job (e.g., word count, data aggregation)
- Can cost much less if run on spot instances instead of on-demand
- By simulating job runtime, data size, and instance pricing
- And displaying the cost difference clearly with easy-to-read charts

---

## ⚙️ Tech Stack

- **Language:** Python (≥3.8)
- **Processing:** PySpark
- **Platform:** Azure Databricks
- **Visualization:** matplotlib
- **Version Control:** Git + GitHub
- **Data:** Static CSV sample + JSON pricing file

---

## 📂 Project Structure
cost-optimizer-simulation/
├── notebooks/
│ └── main_simulation_notebook.ipynb
├── src/
│ ├── spark_simulator.py
│ ├── cost_calculator.py
│ ├── visualization.py
├── data/
│ ├── pricing.json
│ └── sample_data.csv
├── README.md
└── requirements.txt

