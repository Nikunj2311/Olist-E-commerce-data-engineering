# Databricks notebook source
spark


# COMMAND ----------

storage_account = "olivdatads"
application_id = "a8b1a081-eb2f-4dce-ba59-d5aaec5e1fd4"
directory_id = "2dada452-9fe8-4e3d-a53a-80deb9f70432"

spark.conf.set(f"fs.azure.account.auth.type.{storage_account}.dfs.core.windows.net", "OAuth")
spark.conf.set(f"fs.azure.account.oauth.provider.type.{storage_account}.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set(f"fs.azure.account.oauth2.client.id.{storage_account}.dfs.core.windows.net", application_id)
spark.conf.set(f"fs.azure.account.oauth2.client.secret.{storage_account}.dfs.core.windows.net", "9Jk8Q~gk0h6MQkzssUw1Qu4ItrJZvFn1Lf3ftcvY")
spark.conf.set(f"fs.azure.account.oauth2.client.endpoint.{storage_account}.dfs.core.windows.net", f"https://login.microsoftonline.com/{directory_id}/oauth2/token")

# COMMAND ----------

customers_df=spark.read.option("header", True).option("inferSchema", True).csv(f"abfss://olistdata@olivdatads.dfs.core.windows.net/bronze/olist_customers_dataset.csv")
display(customers_df)

# COMMAND ----------

geolocation_df = spark.read.option("header", True).option("inferSchema", True).csv("abfss://olistdata@olivdatads.dfs.core.windows.net/bronze/olist_geolocation_dataset.csv")
order_item= spark.read.option("header", True).option("inferSchema", True).csv("abfss://olistdata@olivdatads.dfs.core.windows.net/bronze/olist_order_items_dataset.csv")
payment_df= spark.read.option("header", True).option("inferSchema", True).csv("abfss://olistdata@olivdatads.dfs.core.windows.net/bronze/olist_order_payments_dataset.csv")
reviews_df= spark.read.option("header", True).option("inferSchema", True).csv("abfss://olistdata@olivdatads.dfs.core.windows.net/bronze/olist_order_reviews_dataset.csv")
order_list= spark.read.option("header", True).option("inferSchema", True).csv("abfss://olistdata@olivdatads.dfs.core.windows.net/bronze/olist_orders_dataset.csv")
product_df= spark.read.option("header", True).option("inferSchema", True).csv("abfss://olistdata@olivdatads.dfs.core.windows.net/bronze/olist_products_dataset.csv")
sellers_df= spark.read.option("header", True).option("inferSchema", True).csv("abfss://olistdata@olivdatads.dfs.core.windows.net/bronze/olist_sellers_dataset.csv")


# COMMAND ----------

from pymongo import MongoClient
import pandas as pd

# COMMAND ----------

# importing module
from pymongo import MongoClient

hostname = "s8txzq.h.filess.io"
database = "olistdataNoSQL_designelse"
port = "27018"
username = "olistdataNoSQL_designelse"
password = "82f3523acf326bc6656a340ce1a51cd23e047089"

uri = "mongodb://" + username + ":" + password + "@" + hostname + ":" + port + "/" + database

# Connect with the portnumber and host
client = MongoClient(uri)

# Access database
mydatabase = client[database]
mydatabase


# COMMAND ----------

collection=mydatabase['product_category_translation']
mongo_data=pd.DataFrame(list(collection.find()))
mongo_data

# COMMAND ----------

mongo_data.drop('_id',axis=1,inplace=True)
mongo_spark_df=spark.createDataFrame(mongo_data)
display(mongo_spark_df)

# COMMAND ----------

display(product_df)

# COMMAND ----------

display(mongo_data)

# COMMAND ----------

from pyspark.sql.functions import col,to_date,datediff,current_date,when

# COMMAND ----------

def clean_datafram(df,name):
    print("Cleaming"+name)
    return df.dropDuplicates().na.drop('all')
order_df=clean_datafram(order_list,'order')
product_df=clean_datafram(product_df,'product')
payment_df=clean_datafram(payment_df,'payment')
review_df=clean_datafram(reviews_df,'review')
sellers_df=clean_datafram(sellers_df,'sellers')
order_item=clean_datafram(order_item,'order_item')
geolocation_df=clean_datafram(geolocation_df,'geolocation')
customers_df=clean_datafram(customers_df,'customers')
display(order_df)
display(product_df)
display(payment_df)
display(review_df)
display(sellers_df)
display(order_item)
display(geolocation_df)
display(customers_df)

# COMMAND ----------

display(order_df)

# COMMAND ----------

order_df=order_df.withColumn("order_purchase_timestamp",to_date(col("order_purchase_timestamp")))\
    .withColumn("order_delivered_customer_date",to_date(col("order_delivered_customer_date")))\
    .withColumn("order_estimated_delivery_date",to_date(col("order_estimated_delivery_date")))
display(order_df)

# COMMAND ----------

order_df=order_df.withColumn("actual_delivery_time",datediff(col("order_delivered_customer_date"),col("order_purchase_timestamp")))
order_df=order_df.withColumn("estimated_delivery_time",datediff(col("order_estimated_delivery_date"),col("order_purchase_timestamp")))
order_df=order_df.withColumn("delay_time",col("actual_delivery_time")-col("estimated_delivery_time"))
display(order_df)

# COMMAND ----------

order_customer=order_df.join(customers_df,order_df.customer_id==customers_df.customer_id,"left")
order_payment=order_customer.join(payment_df,order_customer.order_id==payment_df.order_id,"left")
order_item_df=order_payment.join(order_item,"order_id","left")
order_product=order_item_df.join(product_df,"product_id","left")
order_seller=order_product.join(sellers_df,"seller_id","left")
order_review=order_seller.join(review_df,"order_id","left")

# COMMAND ----------

display(order_product)
display(sellers_df)

# COMMAND ----------

display(order_review)

# COMMAND ----------

final_df=order_review.join(mongo_spark_df, "product_category_name", "right")
display(final_df)

# COMMAND ----------

def remove_duplicate(df):
    columns=df.columns
    seen_column=set()
    drop_column=[]
    for column in columns:
        if column in seen_column:
            drop_column.append(column)
        else:
            seen_column.add(column)
    return df.drop(*drop_column)
final_df=remove_duplicate(final_df) 
final_df=final_df.drop("Delay Time")

# COMMAND ----------

final_df.write.mode("overwrite").parquet("abfss://olistdata@olivdatads.dfs.core.windows.net/silver")