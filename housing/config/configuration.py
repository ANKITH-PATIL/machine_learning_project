from housing.entity.config_entity import data_ingestion_config,data_transformation_config,data_validation_config,\
    model_evaluation_config,model_training_config,model_pusher_config,training_pipeline_config

from housing.util.util import read_yaml_file

from housing.constant import *
 

class configuration:

    def __init__(self,
        config_file_path:str=CONFIG_FILE_PATH,
        current_time_stamp:str=CURRENT_TIME_STAMP
        )->None:
        self.config_info=read_yaml_file(filepath=config_file_path)
        self.training_pipeline_config=self.get_training_pipeline_config()
        
        



    def get_data_ingestion_config(self)-> data_ingestion_config:
        pass

    def get_data_validation_config(self)->data_validation_config:
        pass

    def get_data_transformation_config(self) -> data_transformation_config:
       pass 

    def get_model_trainer_config(self)->model_training_config:
        pass

    def get_model_evaluation_config(self)->model_evaluation_config:
        pass

    def get_model_pusher_config(self)->model_pusher_config:
        pass
    
    def get_training_pipeline_config(self)-> training_pipeline_config:
        return 

    