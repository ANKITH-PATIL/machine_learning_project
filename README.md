# machine_learning_project

# create conda environment
'''

conda create -p venv python==3.7 -y

# -p used bcoz we provide the prefix for the name of the folder we create
# if -n is used we create an virtual env folder in the anaconda directory 

# but we create an virtual env along with the project 

first check whether u have the conda environment
''' 

To set up a CI/CD pipeline we need 3 information:
1. HEROKU email-id : ankithpatilbusiness@gmail.com
2. heroku API : 957321a3-aaea-4d90-a826-e9c5a897db68
3. HEROKU App : machine-learning-cicd-pipeline



Dockerfile :

''' For creating a Dockerimage we need to give set of instructions '''

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