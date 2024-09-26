from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)-> List[str]:
    '''
    this function will return the list ofg requireemnts
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        #added to ignore ie from requirement.txt which was adde to run setup.py
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements



setup(
    name='mlproject',
    version='0.0.1',
    autor='shakti',
    author_email='rathoreshakti1993@gmail.com',
    pacvkage=find_packages(),
    #install_requires=['pandas','numpy','seaborn']
    install_required=get_requirements('requirements.txt')

)