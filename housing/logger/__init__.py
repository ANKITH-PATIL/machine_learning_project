import logging
#normally in industry scenario we try to keep logs which are 3 months older for project maintanaince  
# we can use script based on the data time stamp  

from datetime import datetime
import os
import pandas as pd
from housing.constant import get_current_time_stamp


LOG_DIR="logs"

CURRENT_TIME_STAMP=  f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

LOG_FILE_NAME=f"log_{CURRENT_TIME_STAMP}.log"


os.makedirs(LOG_DIR,exist_ok=True)  #exist ok shows that if the housing logs are already created then dont create it 

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
#format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',

#here name gives the name of the dir, levelname gives whether its info ,debug etc

format='[%(asctime)s]^;%(levelname)s^;%(lineno)d^;%(filename)s^;%(funcName)s()^;%(message)s',

# here the separater is custom given so as to make the separation 
# later use that separation to form the dataframe in the next function

level=logging.INFO
)


def get_log_dataframe(file_path):
    data=[]
    with open(file_path) as log_file:
        for line in log_file.readlines():
            data.append(line.split("^;"))

    log_df = pd.DataFrame(data)
    columns=["Time stamp","Log Level","line number","file name","function name","message"]
    log_df.columns=columns
    
    log_df["log_message"] = log_df['Time stamp'].astype(str) +":$"+ log_df["message"]

    return log_df[["log_message"]]



