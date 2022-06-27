from collections import namedtuple


data_ingestion_config=namedtuple("data_ingestion_config",
["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])

data_validation_config=namedtuple("data_validation_config",["schema_file_path"])

data_transformation_config=namedtuple("data_transformation_config",[
    "add_bedroom_per_room","tranformed_test_dir","transformed_train_dir","preprocessed_object_filepath"
])


model_training_config=namedtuple("model_training_config",["trained_model_filepath","base_accuracy"])


model_evaluation_config=namedtuple("model_evaluation_config",["model_evaluation_filepath","time_stamp"])


model_pusher_config=namedtuple("model_pusher_config",["export_dir_path"])


training_pipeline_config=namedtuple("training_pipeline_config",["artifact_dir"])


