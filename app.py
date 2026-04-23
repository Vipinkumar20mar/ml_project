from src.ml_project.logger import logging
from src.ml_project.exceptions import CustomException
from src.ml_project.components.data_ingestion import DataIngestion
import sys

if __name__=="__main__":
    logging.info("Starting the prediction pipeline.")
    try:
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
        

    except Exception as e:
        logging.error("An error occurred in the custom exception handler.")
        raise CustomException(e,sys)
    