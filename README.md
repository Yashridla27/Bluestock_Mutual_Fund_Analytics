# Mutual Fund Analytics Capstone Project

## Project Overview

The Mutual Fund Analytics Capstone Project was developed as part of the Bluestock Fintech Internship Program. The project focuses on analyzing mutual fund industry data through ETL processes, Exploratory Data Analysis (EDA), performance evaluation, advanced risk analytics, and interactive Power BI dashboards.

The objective is to transform raw mutual fund datasets into meaningful insights related to fund performance, investor behavior, SIP trends, risk metrics, and industry growth.

---

## Setup Instructions

### Prerequisites

Install the following software before running the project:

* Python 3.10+
* Jupyter Notebook
* Power BI Desktop
* SQLite

### Install Required Packages

```bash
pip install -r requirements.txt
```

---

## Project Structure

```text
Mutual_Fund_Analytics/

├── Data/
│   ├── Raw/
│   ├── Processed/
│   └── db/

├── Notebooks/
│   ├── 01_data_ingestion.py
│   ├── 02_data_cleaning.py
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb

├── scripts/
│   ├── run_pipeline.py
│   ├── create_database.py
│   ├── check_db.py
│   └── helper scripts

├── SQL/
│   ├── schema.sql
│   └── queries.sql

├── Dashboard/

├── Reports/

├── requirements.txt
└── README.md
```

---

## File Descriptions

### Data Folder

Contains all datasets used in the project.

* Raw: Original mutual fund datasets
* Processed: Cleaned and transformed analytical datasets
* db: SQLite database files

### Notebooks Folder

Contains data processing and analytical workflows.

* 01_data_ingestion.py – Loads raw datasets
* 02_data_cleaning.py – Performs ETL and data cleaning
* 03_eda_analysis.ipynb – Exploratory Data Analysis
* 04_performance_analytics.ipynb – Return and performance analysis
* 05_advanced_analytics.ipynb – Risk analytics and advanced metrics

### Scripts Folder

Contains utility and automation scripts.

* run_pipeline.py – Master pipeline execution script
* create_database.py – Creates SQLite database
* check_db.py – Database validation script

### SQL Folder

Contains SQL schema definitions and query files used for database operations.

### Dashboard Folder

Contains the Power BI dashboard file used for visualization and reporting.

### Reports Folder

Contains the final project report, presentation deck, and exported chart images.

---

## How to Run ETL

Execute the master pipeline script:

```bash
python scripts/run_pipeline.py
```

The pipeline performs:

1. Data Ingestion
2. Data Cleaning
3. Dataset Preparation

EDA, Performance Analytics, and Advanced Analytics are available as Jupyter Notebooks for interactive analysis.

---

## How to Open Dashboard

1. Open Power BI Desktop.
2. Navigate to the Dashboard folder.
3. Open the `.pbix` dashboard file.
4. Refresh data if required.
5. Explore the dashboard pages and interactive visualizations.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SQLite
* SQL
* Power BI

---

## Project Outputs

* Cleaned Mutual Fund Datasets
* EDA Insights
* Performance Analytics
* Risk Metrics (Sharpe, Sortino, VaR, CVaR)
* Interactive Power BI Dashboard
* Final Project Report
* Presentation Deck

---

## Author

Yash Ridla

Bluestock Fintech Internship Program
