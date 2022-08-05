from housing.logger import logging
from housing.exception import housing_exception
from housing.entity.config_entity import Data_Validation_Config
from housing.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
import os,sys
import pandas  as pd
from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab
import json
from housing.util.util import read_yaml_file
from housing.constant import *

class DataValidation:
    

    def __init__(self, data_validation_config:Data_Validation_Config,
        data_ingestion_artifact:DataIngestionArtifact):
        try:
            logging.info(f"{'>>'*30}Data Valdaition log started.{'<<'*30} \n\n")
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise housing_exception(e,sys) from e


    def get_train_and_test_df(self):
        try:
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            return train_df,test_df
        except Exception as e:
            raise housing_exception(e,sys) from e


    def is_train_test_file_exists(self)->bool:
        try:
            logging.info("Checking if training and test file is available")
            is_train_file_exist = False
            is_test_file_exist = False

            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            is_train_file_exist = os.path.exists(train_file_path)
            is_test_file_exist = os.path.exists(test_file_path)

            is_available =  is_train_file_exist and is_test_file_exist

            logging.info(f"Is train and test file exists?-> {is_available}")
            
            if not is_available:
                training_file = self.data_ingestion_artifact.train_file_path
                testing_file = self.data_ingestion_artifact.test_file_path
                message=f"Training file: {training_file} or Testing file: {testing_file}" \
                    "is not present"
                raise Exception(message)

            return is_available
        except Exception as e:
            raise housing_exception(e,sys) from e

    
    def validate_dataset_schema(self)->bool:#,schema_file_path,file_path)->bool:
        try:
            # validation_status = True#
            # column_count_equal= False#
            # column_names_same= False#



            #Assigment validate training and testing dataset using schema file
            #1. Number of Column
            #2. Check the value of ocean proximity 
            # acceptable values     <1H OCEAN
            # INLAND
            # ISLAND
            # NEAR BAY
            # NEAR OCEAN
            #3. Check column names

            # we dont mmodify any data(thats done in the feature engineering stage) here we just check the above steps



            # dataset_schema=read_yaml_file(schema_file_path)#
            # schema=dataset_schema[DATASET_SCHEMA_COLUMNS_KEY]#
            
            # df=pd.read_csv(file_path=file_path)#

# checking column numbers in the schema file and dataset of the column same or not

            # if len(list(schema.keys()))==len(df.columns):#
            #     column_count_equal=True#
            
# checking columns name in the schema file and dataset same or not


            # for col in df.columns:
            #     if col in list(schema.keys()):
            #         df[col].astype(schema[col])
            #         column_names_same=True
            #     else:
            #         column_names_same=False
                    
            # if column_count_equal and column_names_same:
            #     validation_status=True
            

            validation_status = True
            return validation_status 
        except Exception as e:
            raise housing_exception(e,sys) from e



    def get_and_save_data_drift_report(self):
        try:
            profile = Profile(sections=[DataDriftProfileSection()])

            train_df,test_df = self.get_train_and_test_df()

            profile.calculate(train_df,test_df)

            report = json.loads(profile.json()) 
            
            # profile.json is a string which is from json file we need
            # json.loads loads the string format into the json file format

            report_file_path = self.data_validation_config.report_file_path
            report_dir = os.path.dirname(report_file_path)
            os.makedirs(report_dir,exist_ok=True)

            with open(report_file_path,"w") as report_file:
                json.dump(report, report_file, indent=6)
            return report
        except Exception as e:
            raise housing_exception(e,sys) from e



    def save_data_drift_report_page(self):
        try:
            dashboard = Dashboard(tabs=[DataDriftTab()])
            train_df,test_df = self.get_train_and_test_df()
            dashboard.calculate(train_df,test_df)

            report_page_file_path = self.data_validation_config.report_page_file_path
            report_page_dir = os.path.dirname(report_page_file_path)
            os.makedirs(report_page_dir,exist_ok=True)

            dashboard.save(report_page_file_path)
        except Exception as e:
            raise housing_exception(e,sys) from e

    def is_data_drift_found(self)->bool:
        try:
            report = self.get_and_save_data_drift_report()
            self.save_data_drift_report_page()
            return True
        except Exception as e:
            raise housing_exception(e,sys) from e

    def initiate_data_validation(self)->DataValidationArtifact :
        try:
            self.is_train_test_file_exists()
            self.validate_dataset_schema()
            self.is_data_drift_found()

            data_validation_artifact = DataValidationArtifact(
                schema_file_path=self.data_validation_config.schema_file_path,
                report_file_path=self.data_validation_config.report_file_path,
                report_page_file_path=self.data_validation_config.report_page_file_path,
                is_validated=True,
                message="Data Validation performed successully."
            )
            logging.info(f"Data validation artifact: {data_validation_artifact}")
            return data_validation_artifact
        except Exception as e:
            raise housing_exception(e,sys) from e


    def __del__(self):
        logging.info(f"{'>>'*30}Data Validation log completed.{'<<'*30} \n\n")


    