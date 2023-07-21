import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled=preprocessor.transform(features)

            pred=model.predict(data_scaled)
            return pred
            

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self,
                 cement :float,
                 blastFurnace:float,
                 flyAsh:float,
                 water:float,
                 superplasticizer:float,
                 courseAggregate:float,
                 fineaggregate :float,
                 age:int,):
        
        self.cement=cement
        self.blastFurnace=blastFurnace
        self.flyAsh=flyAsh
        self.water=water
        self.superplasticizer=superplasticizer
        self.courseAggregate =courseAggregate 
        self.fineaggregate  = fineaggregate 
        self.age = age

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'cement':[self.cement],
                'blastFurnace':[self.blastFurnace],
                'flyAsh':[self.flyAsh],
                'water':[self.water],
                'superplasticizer':[self.superplasticizer],
                'courseAggregate':[self.courseAggregate],
                'fineaggregate':[self.fineaggregate],
                'age':[self.age],
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)


