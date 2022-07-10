from housing.entity.config_entity import Data_Ingestion_Config,Data_Transformation_Config,Data_Validation_Config,\
     Model_Evaluation_Config, Model_Pusher_Config, Model_Training_Config, Training_Pipeline_Config
from housing.util.util import read_yaml_file

from housing.logger import logging
from housing.constant import *

from housing.exception import housing_exception
import os,sys
 

class Configuration:

    def __init__(self,
        config_file_path:str=CONFIG_FILE_PATH,
        current_time_stamp:str=CURRENT_TIME_STAMP
        )->None:
        try:
            self.config_info=read_yaml_file(filepath=config_file_path)
            self.training_pipeline_config=self.get_training_pipeline_config()
            self.time_stamp=current_time_stamp

        except Exception as e:
            raise housing_exception(e,sys) from e

        
        



    def get_data_ingestion_config(self)-> Data_Ingestion_Config:

        #this will create data ingestion folder inside the artifacts folder:
        # artifacts >> data ingestion >> timestamp >> all foldeds(tgz, raw data , ingested data >>(train, test))
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_ingestion_artifact_dir=os.path.join(
                artifact_dir,
                DATA_INGESTION_ARTIFACT_DIR,
                self.time_stamp
            )
            data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]
            
            dataset_download_url = data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY]
            tgz_download_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY]
            )
            raw_data_dir = os.path.join(data_ingestion_artifact_dir,
            data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY]
            )

            ingested_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_INGESTED_DIR_NAME_KEY]
            )
            ingested_train_dir = os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY]
            )
            ingested_test_dir =os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY]
            )

            data_ingestion_config=Data_Ingestion_Config(
                dataset_download_url=dataset_download_url, 
                tgz_download_dir=tgz_download_dir, 
                raw_data_dir=raw_data_dir, 
                ingested_train_dir=ingested_train_dir, 
                ingested_test_dir=ingested_test_dir
            )

            
            logging.info(f"Data Ingestion config:{data_ingestion_config}")
            
            return data_ingestion_config

        except Exception as e:
            raise housing_exception(e,sys) from e

         

    def get_data_validation_config(self)->Data_Validation_Config:
        pass

    def get_data_transformation_config(self) -> Data_Transformation_Config:
       pass 

    def get_model_trainer_config(self)->Model_Training_Config:
        pass

    def get_model_evaluation_config(self)->Model_Evaluation_Config:
        pass

    def get_model_pusher_config(self)->Model_Pusher_Config:
        pass
    
    def get_training_pipeline_config(self)->Training_Pipeline_Config:
        try:
            training_pipeline_config=self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir=os.path.join(ROOT_DIR,training_pipeline_config[TRAINING_PIPELINE_CONFIG_NAME_KEY],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_CONFIG_KEY]
            )
            training_pipeline_config=Training_Pipeline_Config(artifact_dir=artifact_dir)
            logging.info(f"Training pipeline config: {training_pipeline_config}")
            return training_pipeline_config

            #all the folders of the pipeline will be contained in this artifact folder

            #this folder will contain all the above output folders of the
            # above components 



        except  Exception as e:
            raise housing_exception(e,sys) from e

         

    