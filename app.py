
from flask import Flask

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])

def index():
    return "Starting Machine Learning Project and checking for the second time for checking whether we have established complete CICD pipeline"

if __name__=="__main__":
    app.run(debug=True)

  