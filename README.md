# machine_learning_project
Application URL:
[HousingPredictor](put the heroku appliaction link)

# create conda environment
```

conda create -p venv python==3.7 -y

# -p used bcoz we provide the prefix for the name of the folder we create
# if -n is used we create an virtual env folder in the anaconda directory 

# but we create an virtual env along with the project 

first check whether u have the conda environment
``` 

To set up a CI/CD pipeline we need 3 information:
1. HEROKU email-id : ankithpatilbusiness@gmail.com
2. heroku API : 957321a3-aaea-4d90-a826-e9c5a897db68
3. HEROKU App : machine-learning-cicd-pipeline



Dockerfile :

``` For creating a Dockerimage we need to give set of instructions ```

docker image will be having smaller version of the python3.7 will be installed int he linux based system 

we create another file named dockerignore wherin we mentions the files which dont ant to be present in the in the dockerimage
like venv/


Creating conda environment
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
```
OR 
```
conda activate venv
```

```
pip install -r requirements.txt
```

To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url 
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMAIL = anishyadav7045075175@gmail.com
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME = ml-regression-app

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```

To check running container in docker
```
docker ps
```

Tos stop docker conatiner
```
docker stop <container_id>
```

no need to type pip install -r requirements.txt after typing the following command
```
python setup.py install
```

```
-e . this will install all the packages present in the folders like housing
     also it runs the setup file internally
     
```

to run jupyter notebook commands

```
pip install ipykernel
```

```
Data versioning :
```

```
every time we run the program we create a new file based on specific timestamp thus thse different times have resulted into different data versions
```

```
INTERVIEW QUESTION:
 where have u done hypothesis testing in the pipeline? 
```
```
when i was retraining my model, thats when i had done hypothesis testing to compare the distribution of the dataset by comparing the old training dataset and the new training dataset and we used the from scipy.stats import ks_2samp module and for further understanding of this module check out the example3.ipynb for how it exactly works

also if the output of the above module is 1 then we consider that the distribution of the data is similar and we conclude that there is no data drift 
```

```
refrences- Sources :
```
```
mlops google cloud search this find the best material for knowing the pipeline of mlops
``` 

```
@staticmethod
```
```
when u r not using any information from the self or the init constructor of a class

u dont need to declare the first parameter as the self in the function of static method
we can call this function by just using the class and not giving the input values of the class which are present in the init constructor
we can this function easily without any issue

if we want to call the fucntion in a class without initialising an object this method is better
```

```
error: make sure that the data validation config contains the schema.dir as the part of its dictionary and see to it that it will reflect in the subsequent programs
``` 
```
Errors which i have faced:
1. error in the config entity named tuple of the component 

2. error in the config.yaml file of not defining the schema

3. error in naming the read_yaml_file(filepath) keyword error
```

```
FYI:

1.  transformed_train_file_path='c:\\Users\\Ankith\\machine_learning_project\\housing\\artifact\\data_transformation\\2022-07-22_10-42-23\\transformed_data\\train\\housing.npz',

contains the np array train file likewise it also has the test file
```

```
Entity >>> model_factory.py:

it can dynamically train any kind of model
```

```
u have written the model factory to ease the process of finding the best machine learning model
```
```
model evaluation >>> will check the new models performance as compared to the present a
                     and if better then will proceed to the model pusher component

model pusher >>> will push the path where the trained model is loacted to saved model folder where it is saved
it can also send the models to the cloud as well
```

```
Re-training : done in the model evaluation component check for detailed understanding
```
```
Q- if u change the preprocessing steps or feature engineering for new models subsequently thwn no need to manually 
     those changes as we are keeping the model preprocessing and model training together 
     CHECK OUT THE 9th JULY CLASS

     so no isssue then thats why we have done this type of combination
     only unless the structure of the data is changed like adding a column or deleting a column changing the datatype of the column 
     then only we have to train the model from the starting and the base models would become irrelevant 
```

```
uploading model.pkl file to the S3/GCP/AZURE BLOB :

1. make 2 functions in the utils folder and import it in the model pusher component
2. the 2 functions are: a. to load model from the s3 bucket
                        b. to save the model into s3 bucket


