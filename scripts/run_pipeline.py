"""
Master Pipeline Runner

Runs the core ETL workflow:
1. Data Ingestion
2. Data Cleaning
"""

import subprocess

subprocess.run(["python", "../Notebooks/01_data_ingestion.py"])
subprocess.run(["python", "../Notebooks/02_data_cleaning.py"])

print("Pipeline Completed Successfully!")