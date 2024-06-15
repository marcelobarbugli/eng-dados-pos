<h1 align="center"> Top 10 restaurants/cities with most RED violations - AWS S3, Amazon EMR, Spark (PySpark and SQL) Lab. </h1>

## With Amazon EMR you can set up a cluster to process and analyze data with big data frameworks in just a few minutes. 

This repository shows you how to launch a sample cluster using Spark, and how to run a simple PySpark script stored in an Amazon S3 bucket. 
It covers essential Amazon EMR tasks in three main workflow categories: Plan and Configure, Manage, and Clean Up.

[!IMPORTANT INFO]:
- ***Download 'King County Open Data' dataset and follow tutorial instructions.***

## Prerequisites

- Apache Spark
- Python 3.x
- Necessary permissions to read/write to specified S3 buckets
- Tutorial: Getting started with Amazon EMR (https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html)
- Dataset: King County Open Data: Food Establishment Inspection Data (https://data.kingcounty.gov/Health-Wellness/Food-Establishment-Inspection-Data/f29f-zza5/about_data)

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/marcelobarbugli/eng-dados-pos.git
    cd eng-dados-pos.git
    ```

2. Install the required dependencies:

    ```bash
    pip install pyspark
    ```

## Usage

The script `calculate_red_violations.py` processes the food establishment inspection data and outputs the results to specified locations.
- top 10 restaurants RED violations
- top 10 cities RED violations

### Parameters

- `data_source`: The URI of your food establishment data CSV. Example: `s3://DOC-EXAMPLE-BUCKET/food-establishment-data.csv`
- `output_uri`: The URI where output is written. Example: `s3://DOC-EXAMPLE-BUCKET/restaurant_violation_results`
- `output_uri_city`: The URI where city violation output is written. Example: `s3://DOC-EXAMPLE-BUCKET/city_violation_results`

### Running the Script

You can run the script by setting the `data_source`, `output_uri`, and `output_uri_city` variables and then calling the `calculate_red_violations` function.

Example:

```python
from pyspark.sql import SparkSession

def calculate_red_violations(data_source, output_uri, output_uri_city):
    """
    Processes sample food establishment inspection data and queries the data to find the top 10 establishments
    with the most Red violations from 2006 to 2020.

    :param data_source: The URI of your food establishment data CSV, such as 's3://DOC-EXAMPLE-BUCKET/food-establishment-data.csv'.
    :param output_uri: The URI where output is written, such as 's3://DOC-EXAMPLE-BUCKET/restaurant_violation_results'.
    :param output_uri_city: The URI where city violation output is written, such as 's3://DOC-EXAMPLE-BUCKET/city_violation_results'.
    """
    with SparkSession.builder.appName("Calculate Red Health Violations").getOrCreate() as spark:
        # Load the restaurant/city violation CSV data
        if data_source is not None:
            restaurants_df = spark.read.option("header", "true").csv(data_source)
            city_df = spark.read.option("header", "true").csv(data_source)

        # Create an in-memory DataFrame to query
        restaurants_df.createOrReplaceTempView("restaurant_violations")
        city_df.createOrReplaceTempView("city_violations")
        
        # Create a DataFrame of the top 10 restaurants/cities with the most Red violations
        top_red_violation_restaurants = spark.sql("""SELECT name, count(*) AS total_red_violations 
          FROM restaurant_violations 
          WHERE `Violation Type` = 'RED' 
          GROUP BY name 
          ORDER BY total_red_violations DESC LIMIT 10""")
        
        top_red_violation_city = spark.sql("""SELECT City, count(*) AS total_red_violations 
          FROM city_violations 
          WHERE `Violation Type` = 'RED' 
          GROUP BY City 
          ORDER BY total_red_violations DESC LIMIT 10""")

        # Write the results to the specified output URI
        top_red_violation_restaurants.write.option("header", "true").mode("overwrite").csv(output_uri)
        top_red_violation_city.write.option("header", "true").mode("overwrite").csv(output_uri_city)

data_source = 's3://emr-s3-bucket2024/Food_Establishment_Inspection_Data_20240612.csv'
output_uri = 's3://emr-s3-bucket2024/saida/restaurant_violations_results'
output_uri_city = 's3://emr-s3-bucket2024/saida/city_violations_results'

calculate_red_violations(data_source, output_uri, output_uri_city)


This README file provides a detailed guide on how to use the `calculate_red_violations.py` script, including prerequisites, installation steps, usage,
and example code.
```
<h5 align="center"> *Project developed by: Marcelo Dozzi Barbugli | Date: 06/14/2024 | Poli-USP: Especialização em Engenharia de Dados - NoSQL lab </h5>
