# 🚀 End-to-End Data Pipeline for Olist E-Commerce Data using Azure

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-FF9900?style=for-the-badge&logo=apache-spark&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=sql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=power-bi&logoColor=black)

---

## 🌟 Project Overview
This project demonstrates an **end-to-end data engineering pipeline** for Olist E-commerce data using **Azure cloud services**.  
The pipeline automates **data ingestion, transformation, and storage**, making it ready for **analytics and business insights**.

---

## 🖼️ Architecture Diagram
<img width="3437" height="1842" alt="Architecture Diagram" src="https://github.com/user-attachments/assets/15fb0aae-6f84-48cf-a836-bcfe3636f10b" />

---

## 🛠️ Tech Stack
- **Azure Data Factory** – Data ingestion & orchestration  
- **Azure Data Lake Storage (Gen2)** – Raw & processed data storage  
- **Azure Databricks (PySpark)** – Data cleaning & transformation  
- **Azure Synapse Analytics** – Data warehousing & querying  
- **Power BI** – Optional visualization & dashboards  

---

## 🔄 Pipeline Flow

```mermaid
flowchart LR
    A[Raw Data Source] --> B[Azure Data Factory]
    B --> C[Bronze Layer - Data Lake Storage]
    C --> D[Silver Layer - Databricks Transformation]
    D --> E[Gold Layer - Synapse Analytics]
    E --> F[Power BI Dashboards]
```
1. Data Ingestion – ADF pulls raw data into Bronze Layer

2. Data Cleaning & Transformation – Databricks (PySpark) processes data into Silver Layer

3. Data Warehousing – Cleaned data loaded into Gold Layer (Synapse Analytics)

4. Visualization  – Power BI dashboards display insights


## 💡 Key Features

* Fully automated ETL pipeline using Azure services

* Implements Medallion Architecture (Bronze → Silver → Gold)

* Scalable & production-ready cloud pipeline

* Data validation & schema enforcement in Databricks

## 🧠 Skills Learned / Highlights

* Azure Data Engineering (ADF, Databricks, Synapse, ADLS)

* PySpark & SQL for large-scale data processing

* ETL Pipeline Design & Data Warehousing

* Cloud orchestration & Medallion Architecture implementation

## 🎬 Demo / Screenshots

### 🧩 Azure Data Factory Pipeline
![ADF Pipeline](screenshot/pipline_flow.png)

### ⚙️ Databricks Data Transformation
![Databricks Transformation](screenshot/data_brick_transformation.png)

### 🧮 Azure Synapse Analytics
![Synapse Query](screenshot/synapse_view.png)

### 📊 Power Bi Dashboard
![Olist E-commerce Sales and Review Dashboard Snapshot](screenshot/Power_bi_dashboard.png)


## ⚡ How to Run / Setup
1. Clone the repository
2. Set up Azure Data Lake Storage & Databricks workspace
3. Run Data Factory pipelines
4. Connect Synapse & visualize in Power BI

# 🏆 Conclusion / Outcome

This project demonstrates a real-world, scalable data engineering pipeline, transforming raw e-commerce data into structured, analytics-ready datasets.
It highlights cloud-based ETL, transformation, and warehouse design, showcasing skills required for data engineering roles.

