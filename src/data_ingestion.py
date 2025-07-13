import os
import pandas as pd
from google.cloud import storage
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml

logger = get_logger(__name__)

# # extract the data from gcp
class DataIngestion:
    def __init__(self,config):
        self.config = config["data_ingestion"] # will read data_ingestion from yaml file
        self.bucket_name = self.config["bucket_name"]
        self.file_name = self.config["bucket_file_name"]
        self.train_test_ratio = self.config["train_ratio"]

  # create raw directory to store end product of this process
        os.makedirs(RAW_DIR , exist_ok=True)

        logger.info(f"Data Ingestion started with {self.bucket_name} and file is  {self.file_name}")

# GCP needs a service account key file for authentication.
# Fix: Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
    def download_csv_from_gcp(self):
        try:
            # my storage.Client() was unable to read the data so i used below code
            #os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\Lenovo\Downloads\testmap-164207-57ca704a658d.json"

            # what was the reason set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\Lenovo\Downloads\testmap-164207-57ca704a658d.json
            # No spaces around the equal sign and no quotes unless the path has spaces but i gave the space that was wrong.

            client = storage.Client() # initialize storage client
            bucket = client.bucket(self.bucket_name) # specified the bucket name
            blob = bucket.blob(self.file_name)

            blob.download_to_filename(RAW_FILE_PATH)  # whatever is stored in blob it will download in rawfilepath

            logger.info(f"CSV file is sucesfully downloaded to {RAW_FILE_PATH}")

        except Exception as e:
            logger.error("Error while downloading the csv file")
            raise CustomException("Failed to downlaod csv file ", e)
        
    def split_data(self):
        try:
            logger.info("Starting the splitting process")
            data = pd.read_csv(RAW_FILE_PATH)
            train_data , test_data = train_test_split(data , test_size=1-self.train_test_ratio , random_state=42)

            train_data.to_csv(TRAIN_FILE_PATH)
            test_data.to_csv(TEST_FILE_PATH)

            logger.info(f"Train data saved to {TRAIN_FILE_PATH}")
            logger.info(f"Test data saved to {TEST_FILE_PATH}")
        
        except Exception as e:
            logger.error("Error while splitting data")
            raise CustomException("Failed to split data into training and test sets ", e)
        
    def run(self):

        try:
            logger.info("Starting data ingestion process")

            self.download_csv_from_gcp()
            self.split_data()

            logger.info("Data ingestion completed sucesfully")
        
        except CustomException as ce:
            logger.error(f"CustomException : {str(ce)}")
        
        finally:
            logger.info("Data ingestion completed")

if __name__ == "__main__":
    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()




        

