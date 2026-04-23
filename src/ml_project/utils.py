import os
import sys
from src.ml_project.exceptions import CustomException
from src.ml_project.logger import logging
import pymysql
import mysql.connector
import pandas as pd

from dotenv import load_dotenv

load_dotenv()
host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")

def read_sql_data():
    logging.info("Entered the read_sql_data method or component")
    try:
        mysql_connection= pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
            )
        logging.info("Successfully connected to the database",mysql_connection)
        df=pd.read_sql_query("SELECT * FROM student",mysql_connection)
        print(df.head())
        logging.info("Successfully read the data from the database")
        return df
        
    except Exception as e:
        logging.error("Error occurred in the read_sql_data component")
        raise CustomException(e,sys)
