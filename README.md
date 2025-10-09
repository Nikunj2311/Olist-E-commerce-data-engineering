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
