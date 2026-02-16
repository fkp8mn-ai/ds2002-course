"""
iss.py

ETL pipeline to extract the current ISS location from a public API,
transform it into tabular format, and load it into a CSV file.

Usage:
    python iss.py output.csv
"""

import sys
import os
import logging
import requests
import pandas as pd
from datetime import datetime


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def extract():
    """
    Extract ISS location data from the Open Notify API.

    Returns:
        dict: Parsed JSON response containing ISS location data.
    """
    url = "http://api.open-notify.org/iss-now.json"

    try:
        logger.info("Starting data extraction from ISS API.")
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad status codes
        data = response.json()
        logger.info("Data successfully extracted.")
        return data

    except requests.exceptions.RequestException as e:
        logger.error(f"Error during API request: {e}")
        return None


def transform(data):
    """
    Transform raw JSON ISS data into tabular pandas DataFrame format.

    Args:
        data (dict): Raw JSON data from extract().

    Returns:
        pandas.DataFrame: Single-row DataFrame with formatted timestamp.
    """
    if data is None:
        logger.error("No data received to transform.")
        return None

    try:
        logger.info("Starting data transformation.")

        timestamp = data["timestamp"]
        latitude = data["iss_position"]["latitude"]
        longitude = data["iss_position"]["longitude"]

        # Convert UNIX timestamp to readable format
        readable_time = pd.to_datetime(timestamp, unit="s")

        df = pd.DataFrame([{
            "timestamp": readable_time.strftime("%Y-%m-%d %H:%M:%S"),
            "latitude": float(latitude),
            "longitude": float(longitude)
        }])

        logger.info("Data successfully transformed.")
        return df

    except Exception as e:
        logger.error(f"Error during transformation: {e}")
        return None


def load(df, filename):
    """
    Load transformed data into a CSV file.

    Appends data if file exists, otherwise creates a new file.

    Args:
        df (pandas.DataFrame): Transformed ISS location record.
        filename (str): Output CSV file name.
    """
    if df is None:
        logger.error("No data available to load.")
        return

    try:
        logger.info("Starting load process.")

        if os.path.exists(filename):
            existing_df = pd.read_csv(filename)
            updated_df = pd.concat([existing_df, df], ignore_index=True)
            updated_df.to_csv(filename, index=False)
            logger.info("Data appended to existing CSV file.")
        else:
            df.to_csv(filename, index=False)
            logger.info("New CSV file created and data written.")

    except Exception as e:
        logger.error(f"Error during load process: {e}")


def main():
    """
    Main ETL workflow controller.
    """
    if len(sys.argv) != 2:
        logger.error("Usage: python iss.py <output_file.csv>")
        sys.exit(1)

    output_file = sys.argv[1]

    logger.info("ETL pipeline started.")

    raw_data = extract()
    transformed_data = transform(raw_data)
    load(transformed_data, output_file)

    logger.info("ETL pipeline completed successfully.")


if __name__ == "__main__":
    main()
