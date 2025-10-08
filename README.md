# 🛍️ Olist E-commerce Data Engineering Project
This repository documents an end-to-end data engineering pipeline built to process, transform, and analyze the Brazilian Olist E-commerce Public Dataset. The goal is to migrate raw data from various source files into a structured Data Warehouse optimized for Business Intelligence (BI) and Machine Learning (ML) consumption.

# 🎯 Project Goals
The primary objectives of this project were to:

Establish a Robust ETL/ELT Pipeline: Design a scalable and automated pipeline capable of handling large, relational datasets.

Implement a Lakehouse Architecture: Utilize modern cloud storage (Azure Data Lake) combined with Delta Lake for reliability and performance.

Ensure Data Quality and Consistency: Cleanse, standardize, and validate raw data to produce reliable fact and dimension tables.

Create Analytical Data Models: Transform transactional data into star-schema models (Silver and Gold layers) suitable for BI reporting and data science feature engineering.

# ⚙️ Technologies Used
Category	Technology	Purpose
Cloud Platform	Microsoft Azure	Core cloud provider for hosting all resources.
Compute & Orchestration	Azure Synapse Analytics	Used for running Spark/SQL jobs and orchestrating the pipeline.
Storage & Format	Azure Data Lake Storage (ADLS Gen2)	Central storage layer for all data (Raw, Silver, Gold).
Data Engine	Apache Spark / PySpark	Used for scalable data ingestion (E) and transformation (T) operations.
Data Format	Delta Lake	Provides ACID properties (Atomicity, Consistency, Isolation, Durability) and improved performance over Parquet files.
Programming Language	Python / SQL	Python for procedural logic and PySpark transformations; SQL for final data modeling and querying.
Secret Management	Azure Key Vault / Databricks Secrets	Securely storing credentials (like Service Principal Client Secrets).


# 🏗️ Data Architecture (The Lakehouse Layers)
The project follows a medallion architecture, organizing data into three distinct quality layers:

Layer	Format/Storage	Description
1. Bronze (Raw)	Parquet/CSV on ADLS Gen2	Stores data exactly as it was sourced, with minimal schema validation. It is the immutable landing zone.
2. Silver (Cleaned)	Delta Lake on ADLS Gen2	Data is cleaned, standardized, de-duplicated, and enriched. This layer is the single source of truth for the organization.
3. Gold (Aggregated/Modeled)	Delta Lake on ADLS Gen2	Data is transformed into optimized dimensional models (e.g., Fact Sales, Dim Customer) ready for final BI tools and analytical queries.


# 🧱 Key Data Transformations
The pipeline focuses on processing the key Olist datasets, including:

Order and Customer Integration: Joining and de-duplicating customer and order information to create a canonical Dim Customer table.

Time Series Preparation: Extracting and formatting date/time columns to create a robust Dim Date table.

Fact Table Creation: Building the core Fact Sales table by joining orders, items, and payments, calculating key metrics like Gross Revenue and Shipping Cost.

Feature Engineering: Creating aggregated columns (e.g., Lifetime Value, Order Count) for use in downstream ML models.

# 🚀 How to Run the Project
Clone the Repository:

Bash

git clone https://github.com/Nikunj2311/Olist-E-commerce-data-engineering.git
Setup Azure Credentials: Ensure your Azure Key Vault or Databricks Secret Scope (<scope>) is configured with the necessary Service Principal credentials (Client ID, Secret, and Directory ID).

Run Notebooks: Execute the notebooks sequentially in your Azure Synapse Workspace, following the order of the Data Architecture layers (Bronze -> Silver -> Gold).
