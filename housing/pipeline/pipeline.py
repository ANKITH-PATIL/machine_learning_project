from cmath import e
from distutils.command.config import config
from tkinter import E
from housing.config.configuration import Configuration
from housing.logger import logging
from housing.exception import housing_exception

from housing.entity.artifact_entity import DataIngestionArtifact
from housing.entity.config_entity import Data_Ingestion_Config
from housing.component.data_ingestion import DataIngestion

import os, sys

class Pipeline:

    def __init__(self,config:Configuration=Configuration())-> None:
        try:
            self.config=config
        
        except Exception as e:
            raise housing_exception(e,sys) from e

    def start_data_ingestion(self) -> DataIngestionArtifact:
        #once u call this function then the data ingestion process is initiated 
        
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
    
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise housing_exception(e, sys) from e

    def start_data_validation(self):
        pass

    def start_data_transformation(Self):
        pass

    def start_model_evaluation(self):
        pass

    def model_trainer(self):
        pass

    def start_model_pusher(self):
        pass

    def run_pipeline(self):
        try:
            data_ingestion_artifact=self.start_data_ingestion()
            
            pass
        
        except Exception as e:
            raise housing_exception(e,sys) from e

    