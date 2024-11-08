from setuptools import setup, find_packages
from typing import List


def get_requirements(file_pth:str)->list[str]:
    '''this func will return list of req'''
    requirements = []
    with open(file_pth) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n","")  for req in requirements]
        

setup(
name='mlproject',
version='0.0.1',
author='Daanish Mittal',
author_email='daanishmittal24@gmail.com',
packages=find_packages(), 
install_requires = get_requirements('requirements.txt')  
   
)
