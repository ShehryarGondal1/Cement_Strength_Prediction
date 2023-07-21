import sys
import pandas as pd
from sklearn.model_selection import train_test_split
import os
import logging
from src.exception import CustomException
from src.utils import export_collection_as_dataframe

class IngestionConfig:
    def __init__(self, raw_data_path, train_data_path, test_data_path):
        self.raw_data_path = raw_data_path
        self.train_data_path = train_data_path
        self.test_data_path = test_data_path

# Create an instance of the IngestionConfig class with the appropriate paths
ingestion_config = IngestionConfig(
    raw_data_path="path/to/raw_data.csv",
    train_data_path="path/to/train_data.csv",
    test_data_path="path/to/test_data.csv",
)

class DataIngestion:
    def __init__(self, ingestion_config):
        self.ingestion_config = ingestion_config

    def initiate_data_ingestion(self):
        logging.info("Entered initiate_data_ingestion method of DataIngestion class")

        try:
            df: pd.DataFrame = export_collection_as_dataframe(
                db_name="GondalDB", collection_name="Cement"
            )

            logging.info("Exported collection as a DataFrame")

            # Rename the columns (replace 'old_column_name' with the actual old column names)
            df.rename(columns={
                'Cement (component 1)(kg in a m^3 mixture)': 'cement',
                'Blast Furnace Slag (component 2)(kg in a m^3 mixture)': 'blastFurnace',
                'Fly Ash (component 3)(kg in a m^3 mixture)': 'flyAsh',
                'Water  (component 4)(kg in a m^3 mixture)': 'water',
                'Superplasticizer (component 5)(kg in a m^3 mixture)': 'superplasticizer',
                'Coarse Aggregate  (component 6)(kg in a m^3 mixture)': 'courseAggregate',
                'Fine Aggregate (component 7)(kg in a m^3 mixture)': 'fineaggregate',
                'Age (day)': 'age',
                'Concrete compressive strength(MPa, megapascals)': 'strength',
            }, inplace=True)

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False)

            logging.info("Train test split")
            train_set,test_set=train_test_split(df,test_size=0.20,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )



        except Exception as e:
            logging.info('Error occured in Data Ingestion config')
