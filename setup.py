from xml.etree.ElementTree import VERSION
from setuptools import setup,find_packages
from typing import List


PROJECT_NAME="housing-predictor"
VERSION="0.0.3"
AUTHOR="Ankith Patil"
DESCRIPTION="This is a first FSDS Nov batch Machine Learning Project"
PACKAGES=find_packages() #this finds all the folders where there is __init__ file and returns those folders name 
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """Description: This function is going to return list of requirement mentioned in
    requirements.txt file
    
    return This function is going to return a list which contains 
    the name of the libraries mentioned in requirements.txt file"""

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_file.readlines()

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=PACKAGES,
install_requires=get_requirements_list()
)