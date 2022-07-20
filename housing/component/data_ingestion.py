# the configuration folder just gives the strings of the folder name 
# while config entity folder gives the named tuple of the component
# while the actual folders are created by the component folders like this one 

import sys

from numpy.lib.shape_base import split
from housing.entity.config_entity import Data_Ingestion_Config
from housing.exception import housing_exception
import os, sys
import tarfile
from six.moves import urllib
import pandas as pd
import numpy as np

from sklearn.model_selection import StratifiedShuffleSplit
from housing.logger import logging
from housing.entity.artifact_entity import DataIngestionArtifact

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
    


    def split_data_as_train_test(self)-> DataIngestionArtifact :
        try:
            raw_data_dir=self.data_ingestion_config.raw_data_dir

            file_name= os.listdir(raw_data_dir)[0]

            housing_file_path=os.path.join(raw_data_dir,file_name)

            housing_data_frame=pd.read_csv(housing_file_path)

            # Stratified data split:



            housing_data_frame["income_cat"] = pd.cut(
                housing_data_frame["median_income"],
                bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],
                labels=[1,2,3,4,5]
            ) #np.inf makes anything above 6 to be in the category/label 5 
                #divides the data into groups
                # the bins are created to show that 0 to 1.5 in the median income 
                # will be labeled as category 1 and subsequently the others between the range would be 
                # labeled as categories till 5  
                # for equtable dist. among test and train datasets

                          
            strat_train_set=None
            strat_test_set=None
            split=StratifiedShuffleSplit(n_splits=1,test_size=0.2,random_state=42)

        #see as the distribution is similar for both train and train dataset 
        # this is the reason we use stratified split for train and test data split
        # for equatable distribution of different categories 

        #why dont we use the cross validation methods(like GRIDSEARCH, RANDOMSEARCH) for dividing the test and train data?
        #we dont use CV FOR LARGE DATA also as in CV our test and train data is part of training and testing as part of a GRID 6
        #at some point or other but here the data is not used alternatively as training or testing data


            for train_index,test_index in split.split(housing_data_frame, housing_data_frame["income_cat"]):
                strat_train_set = housing_data_frame.loc[train_index].drop(["income_cat"],axis=1)
                strat_test_set = housing_data_frame.loc[test_index].drop(["income_cat"],axis=1)

            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir,
                                            file_name)

            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir,
                                        file_name)

            if strat_test_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_train_dir,exist_ok=True)
                strat_train_set.to_csv(train_file_path,index=False)
            if strat_test_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir)
                strat_test_set.to_csv(test_file_path,index=False)

            
            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,
                                test_file_path=test_file_path,
                                is_ingested=True,
                                message=f"Data ingestion completed successfully."
                                )
            logging.info(f"Data Ingestion artifact:[{data_ingestion_artifact}]")
            return data_ingestion_artifact

        except Exception as e:
            raise housing_exception(e,sys) from e


        
    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            tgz_file_path =  self.download_housing_data()
            self.extract_tgz_file(tgz_file_path=tgz_file_path)
            return self.split_data_as_train_test()
        except Exception as e:
            raise housing_exception(e,sys) from e


        