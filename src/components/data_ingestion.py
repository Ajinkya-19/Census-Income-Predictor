import os , sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustmeException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
@dataclass
class DataIngestionConfig:
    train_data_path =os.path.join("artifacts/data_ingestion", "train.csv")
    test_data_path =os.path.join("artifacts/data_ingestion", "test.csv")
    raw_data_path =os.path.join("artifacts/data_ingestion", "raw.csv")
    
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info('Data Ingestion started')
        try:
          logging.info("data Reading usinf pandas ")
          data=pd.read_csv(os.path.join("notebook/data","income_cleandata.csv"))
          os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok = True)
          data.to_csv(self.ingestion_config.raw_data_path,index = False)
          logging.info('Data Splitted into train and test set')
          train_set,test_set = train_test_split(data, test_size=0.3, random_state=42)
          train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
          test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)
          
          logging.info('Data Ingestion Completed')
          
          return (
              self.ingestion_config.train_data_path,
              self.ingestion_config.test_data_path
          )
        except Exception as e:
            logging.info('Error occured in data ingestion stage')
            raise CustmeException(e, sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path,test_data_path = obj.initiate_data_ingestion()
    
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data_path,test_data_path)
    #src\components\data_ingestion.py
    
    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
    