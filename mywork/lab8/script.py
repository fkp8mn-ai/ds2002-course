import boto3
import argparse
import logging
import os

logging.basicConfig(level=logging.INFO)

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("input_folder")
    parser.add_argument("destination")
    return parser.parse_args()

def upload(input_folder, destination):
    """Upload results files to S3"""
    try:
        s3 = boto3.client('s3')
        bucket, prefix = destination.split('/', 1)

        for file in os.listdir(input_folder):
            if file.startswith("results") and file.endswith(".csv"):
                path = os.path.join(input_folder, file)
                key = f"{prefix}/{file}"
                s3.upload_file(path, bucket, key)
                logging.info(f"Uploaded {file}")

    except Exception as e:
        logging.error(f"Error: {e}")

def main():
    args = parse_args()
    upload(args.input_folder, args.destination)
    logging.info("Upload process finished")

if __name__ == "__main__":
    main()
