from src.cricket.logger import logging
from src.cricket.exception import CustomException
from src.cricket.components.data_ingestion import DataIngestion
from src.cricket.components.data_ingestion import dataingestionconfig
import sys

if __name__=="__main__":
    logging.info("execution has started")

    try:
       data_ingestion=DataIngestion()
       data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("CustomException")
        raise CustomException(e,sys)
