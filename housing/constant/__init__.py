import os
from datetime import datetime

ROOT_DIR=os.getcwd() #tpo get the current working directory
CONFIG_DIR= "config"
CONFIG_FILE_NAME="config.yaml"
CONFIG_FILE_PATH=os.path.join(ROOT_DIR, CONFIG_DIR,CONFIG_FILE_NAME)


CURRENT_TIME_STAMP=  f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

# Training Pipeline realted variable

TRAINING_PIPELINE_CONFIG_KEY="training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_CONFIG_KEY= "artifact_dir"
TRAINING_PIPELINE_CONFIG_NAME_KEY="pipeline_name"

# Data Ingestion Related variable

DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = "tgz_download_dir"
DATA_INGESTION_INGESTED_DIR_NAME_KEY = "ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY = "ingested_test_dir"

# Data Validation Related Variable

DATA_VALIDATION_CONFIG_KEY="data_validation_config"
DATA_VALIDATION_ARTIFACT_DIR="data_validation"
DATA_VALIDATION_SCHEMA_DIR_KEY="schema_dir"
DATA_VALIDATION_SCHEMA_FILE_NAME_KEY="schema_file_name"
DATA_VALIDATION_REPORT_FILE_NAME="report_file_name"
DATA_VALIDATION_REPORT_PAGE_FILE_NAME_KEY="report_page_file_name"

"report_file_path","report_page_file_path"