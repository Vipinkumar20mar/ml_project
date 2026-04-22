from src.ml_project.logger import logging
from src.ml_project.exceptions import CustomException
import sys

if __name__=="__main__":
    logging.info("Starting the prediction pipeline.")
    try:
        a=1/0

    except Exception as e:
        logging.error("An error occurred in the custom exception handler.")
        raise CustomException(e,sys)
    