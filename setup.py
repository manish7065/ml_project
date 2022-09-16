
from setuptools import setup
from typing import List 

#Declearing variables for setup function
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.2"
AUTHOR = "Manish Kumar"
DESCRIPTION = "This is a sirst FSDS Projrct of ml-project"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    '''
    Description: This function is going to return list of requirement 
    mentioned in requirements.txt file

    return: This function is going to return
    a list which contain name or libraries mentioned in requirements.txt file 
    '''
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")
    



setup(
name = PROJECT_NAME,
versions = VERSION,
author = AUTHOR,
description = DESCRIPTION,
Package = PACKAGES,
install_requires = get_requirements_list(),

)