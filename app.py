
from flask import Flask
import sys
from housing.logger import logging
from housing.exception import housing_exception

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])

def index():

    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing=housing_exception(e,sys)
        logging.info(housing.error_message)
        logging.info("We are testing logging module")
    return "Starting Machine Learning Project and checking for the second time for checking whether we have est.complete CICD pipeline"

if __name__=="__main__":
    app.run(debug=True)

  