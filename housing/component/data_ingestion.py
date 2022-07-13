# the entity config folder just gives the strings of the folder name 
# while the actual folders are created by the component folders like this one 

import sys
from housing.entity.config_entity import Data_Ingestion_Config
from housing.exception import housing_exception
import os, sys
import tarfile
from six.moves import urllib

from housing.logger import logging
from housing.entity.artifact_entity import Da

class DataIngestion:
    
    def __init__(self,data_ingestion_config:Data_Ingestion_Config) -> None:
        try:
               self.data_ingestion_config=data_ingestion_config
               logging.info(f"{'>>'*20}Data Ingestion log started.{'<<'*20} ")

        except Exception as e:
            raise housing_exception(e,sys)

    
    def download_housing_data(self):
        try:
# For extraction of remote url 

            download_url=self.data_ingestion_config.dataset_download_url

# folder location which contains the zip file downloaded

            tgz_download_dir=self.data_ingestion_config.tgz_download_dir

# if the folder location for placing the downloaded file if not there else make it 
            if os.path.exists(tgz_download_dir):
                os.remove(tgz_download_dir)

            os.makedirs(tgz_download_dir,exist_ok=True)

# to extract the exact name of the file which is available at the end of the url 

            housing_file_name=os.path.basename(download_url)

# creates the final folder location where the extraced file would be saved

            tgz_download_file_path=os.path.join(tgz_download_dir,housing_file_name)

            logging.info(f"Downloading file from [{download_url}] into : [{tgz_download_file_path}]")

# downloades the url provided and saves it in the file location provided
        
            urllib.request.urlretrieve(download_url,tgz_download_file_path)

            logging.info(f"file :{tgz_download_file_path} downloaded successfully ")

            return tgz_download_file_path

        except Exception as e:
            raise housing_exception(e,sys)
            

    def extract_tgz_file(self,tgz_file_path:str):
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)

            os.makedirs(raw_data_dir,exist_ok=True)

            logging.info(f"Extracting tgz file: [{tgz_file_path}] into dir: [{raw_data_dir}]")
            with tarfile.open(tgz_file_path) as housing_tgz_file_obj:
                housing_tgz_file_obj.extractall(path=raw_data_dir)
            logging.info(f"Extraction completed")

        except Exception as e:
            raise housing_exception(e,sys) from e
    


    def split_data_as_train_test(self):
        pass

        
    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise housing_exception(e,sys) from e


        