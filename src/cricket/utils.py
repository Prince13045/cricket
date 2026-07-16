import os
import sys
import pandas as pd
import pymysql
from dotenv import load_dotenv

from src.cricket.exception import CustomException
from src.cricket.logger import logging

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")


def read_sql_data():
    logging.info("Reading MySQL started")

    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db
        )

        logging.info("Connection established")

        df = pd.read_sql_query("SELECT * FROM  ipl", mydb)

        print(df.head())

        return df

    except Exception as ex:
        raise CustomException(ex, sys)