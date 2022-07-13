import logging
#normally in industry scenario we try to keep logs which are 3 months older for project maintanaince  
# we can use script based on the data time stamp  

from datetime import datetime
import os

LOG_DIR="housing_logs"

CURRENT_TIME_STAMP=  f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

LOG_FILE_NAME=f"log_{CURRENT_TIME_STAMP}.log"


os.makedirs(LOG_DIR,exist_ok=True)  #exist ok shows that if the housing logs are already created then dont create it 

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
level=logging.INFO
)




