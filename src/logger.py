#Purpose of logger is that any execution happens we should able to log all info,track error
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
#whatever log will get created it will be with respect to the current working directory
#Every file will start with logs along with "logs" file name

os.makedirs(logs_path,exist_ok=True)
#eventhough there is file or folder keep on appending the files inside that whenever we want to create the file

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

#whenever we need to create a log or we want to overwrite this functionality of the login we need to setup config
logging.basicConfig(
    filename=LOG_FILE_PATH,#file name where we want to save it
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",#how message get printed #what format we want to use
    level = logging.INFO,
)

#To check everything working properly
# if __name__ == "__main__":
#     logging.info("Logging has started...")
