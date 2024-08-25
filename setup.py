from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''

    requiments=[]
    with open(file_path) as file_obj:
        requiments=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requiments]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="ML Project",
    version="0.0.1",
    author="Shivam Kumar",
    author_email="shivam4756kumar@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
