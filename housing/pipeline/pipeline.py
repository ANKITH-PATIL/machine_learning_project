#thru pipeline folder we run all the componenets by calling the components file 

from cmath import e
from distutils.command.config import config
from tkinter import E
from housing.config.configuration import Configuration
from housing.logger import logging
from housing.exception import housing_exception

from housing.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact,DataTransformationArtifact
from housing.entity.config_entity import Data_Ingestion_Config,Data_Validation_Config,Data_Transformation_Config
from housing.component.data_ingestion import DataIngestion
from housing.component.data_validation import DataValidation
from housing.component.data_transformation import DataTransformation

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

    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) \
            -> DataValidationArtifact:
        try:
            data_validation = DataValidation(data_validation_config=self.config.get_data_validation_config(),
                                             data_ingestion_artifact=data_ingestion_artifact
                                             )
            return data_validation.initiate_data_validation()
        except Exception as e:
            raise housing_exception(e, sys) from e



    def start_data_transformation(self,
                                  data_ingestion_artifact: DataIngestionArtifact,
                                  data_validation_artifact: DataValidationArtifact
                                  ) -> DataTransformationArtifact:
        try:
            data_transformation = DataTransformation(
                data_transformation_config=self.config.get_data_transformation_config(),
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_artifact=data_validation_artifact
            )
            return data_transformation.initiate_data_transformation()
        except Exception as e:
            raise housing_exception(e, sys) from e


    def start_model_evaluation(self):
        pass

    def model_trainer(self):
        pass

    def start_model_pusher(self):
        pass

    def run_pipeline(self):
        try:
            data_ingestion_artifact=self.start_data_ingestion()
            data_validation_artifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            #return data_validation_artifact
            
        
        except Exception as e:
            raise housing_exception(e,sys) from e

    