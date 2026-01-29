# 📊 Automated Sales Data Pipeline using Airflow and Docker

## 1. Project Overview

This project demonstrates an **end-to-end ETL pipeline** for sales transaction data using **Apache Airflow**, **PostgreSQL**, and **Docker**.

The goal is to ingest raw sales data from a CSV file, clean and validate the data, and load it into a data warehouse table ready for analytical queries.

This project is designed as a **Data Engineering final project**, focusing on:
- Data pipeline orchestration
- Data quality validation
- Reproducibility using Docker

---

## 2. Problem Statement

Retail companies often store sales transactions in CSV or Excel files exported manually from POS systems.

These raw datasets usually:
- Are not schema-standardized
- May contain duplicated transactions
- Lack data quality validation
- Are not directly usable for analytics

Therefore, an automated ETL pipeline is required to:
- Ingest raw data
- Clean and validate data
- Store data in a structured format for analysis

---

## 3. Dataset

- **Dataset name:** Supermarket Sales
- **File:** `Supermarket_sales.csv`
- **Granularity:** Transaction-level (invoice-level)

Key fields:
- Invoice ID
- Date
- Branch / City
- Product line
- Quantity
- Unit price
- Total

---

## 4. Pipeline Architecture
Supermarket_sales.csv
↓
raw_supermarket_sales
↓
clean_supermarket_sales
↓
fact_sales

### Layers:
- **Raw layer:** Stores ingested data without modification
- **Clean layer:** Applies validation and data quality rules
- **Serve layer (Fact table):** Ready for analytical queries

---

## 5. Data Cleaning & Validation Rules

The following rules are applied in the clean layer:

| Rule | Purpose |
|----|--------|
| Quantity > 0 | Logical data validation |
| Unit price > 0 | Logical data validation |
| Total = Quantity × Unit price | Data consistency |
| Remove duplicate Invoice IDs | Prevent double counting |
| Parse Date column | Enable time-based analysis |

---

## 6. Technology Stack

- **Apache Airflow** – Workflow orchestration
- **PostgreSQL** – Data storage
- **Docker & Docker Compose** – Containerized deployment
- **Python** – ETL logic
- **Pandas & SQLAlchemy** – Data processing and DB interaction

---

## 7. Project Structure

sales_etl_project/
├── dags/
│ └── sales_etl_dag.py
├── scripts/
│ ├── extract.py
│ ├── clean.py
│ ├── load.py
│ └── db.py
├── data/
│ └── Supermarket_sales.csv
├── docker-compose.yml
├── requirements.txt
└── README.md

---

## 8. Airflow DAG

- **DAG name:** `sales_etl_pipeline`
- **Schedule:** Manual trigger
- **Tasks:**
  1. Extract raw data from CSV
  2. Clean and validate data
  3. Load data into fact table

The DAG is triggered via the **Airflow Web UI**.

---

## 9. How to Run the Project

### 1️⃣ Start services using Docker
```bash```
docker compose up -d
2️⃣ Open Airflow UI

URL: http://localhost:8080

Username: admin

Password: admin

3️⃣ Trigger the DAG

Enable the DAG

Click Trigger DAG

Monitor task execution in Graph view
----

## 10. Example Queries

Row count validation
SELECT COUNT(*) FROM fact_sales;

Revenue by branch
SELECT branch, SUM(total) AS revenue
FROM fact_sales
GROUP BY branch;

Monthly revenue
SELECT DATE_TRUNC('month', "Date") AS month, SUM(total)
FROM fact_sales
GROUP BY month
ORDER BY month;

## 11. Conclusion

This project demonstrates how to build a reproducible and automated ETL pipeline using modern Data Engineering tools.

The pipeline ensures:

Data quality and consistency

Clear separation of pipeline layers

Easy orchestration and monitoring with Airflow

The resulting dataset is ready for analytical and business intelligence use cases.