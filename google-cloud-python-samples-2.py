import os
from google.cloud import bigquery
from google.cloud import storage

# Initialize Google Cloud services
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your-service-account-key.json"

# Function to interact with BigQuery
def query_bigquery():
    client = bigquery.Client()
    query = """
    SELECT name, population
    FROM `bigquery-public-data.usa_names.usa_1910_2013`
    WHERE state = 'TX'
    ORDER BY population DESC
    LIMIT 10;
    """
    query_job = client.query(query)

    print("Top 10 names in Texas by population:")
    for row in query_job:
        print(f"Name: {row.name}, Population: {row.population}")

# Function to upload a file to Cloud Storage
def upload_to_storage(bucket_name, source_file_name, destination_blob_name):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

if __name__ == "__main__":
    print("Running Google Cloud SDK Sample Application")

    # BigQuery example
    query_bigquery()

    # Cloud Storage example
    bucket_name = "your-bucket-name"
    source_file_name = "local-file.txt"
    destination_blob_name = "remote-file.txt"

    upload_to_storage(bucket_name, source_file_name, destination_blob_name)
