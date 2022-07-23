#these provide structure to the configuration folder or package

from collections import namedtuple


Data_Ingestion_Config=namedtuple("Data_Ingestion_Config",
["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])

Data_Validation_Config=namedtuple("Data_Validation_Config",["schema_file_path","report_file_path","report_page_file_path"])

Data_Transformation_Config=namedtuple("Data_Transformation_Config",[
    "add_bedroom_per_room","transformed_test_dir","transformed_train_dir","preprocessed_object_file_path"
])


Model_Trainer_Config=namedtuple("Model_Training_Config",["trained_model_filepath","base_accuracy"])


Model_Evaluation_Config=namedtuple("Model_Evaluation_Config",["model_evaluation_filepath","time_stamp"])


Model_Pusher_Config=namedtuple("Model_Pusher_Config",["export_dir_path"])


Training_Pipeline_Config=namedtuple("Training_Pipeline_Config",["artifact_dir"])


