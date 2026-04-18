import logging
from google.cloud import storage

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # show all logs
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def create_bucket(bucket_name):
    project_id = "bwt-learning-2024-493704"

    try:
        logging.info("Starting bucket creation process")

        # ⚠️ WARNING example
        if " " in bucket_name:
            logging.warning("Bucket name contains spaces (invalid for GCP)")

        client = storage.Client(project=project_id)

        bucket = client.bucket(bucket_name)
        bucket.storage_class = "STANDARD"

        new_bucket = client.create_bucket(bucket, location="US")

        logging.info(f"Bucket created: {new_bucket.name}")
        logging.info(f"Location: {new_bucket.location}")
        logging.info(f"Storage Class: {new_bucket.storage_class}")

    except Exception as e:
        # ❌ ERROR example
        logging.error(f"Error creating bucket: {e}")


# ✅ 1. INFO (success case)
create_bucket("buck1-unique-abc123")

# ⚠️ 2. WARNING (invalid name)
create_bucket("buck invalid name")

# ❌ 3. ERROR (duplicate bucket)
create_bucket("buck1-unique-abc123")