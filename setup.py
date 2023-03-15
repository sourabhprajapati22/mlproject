from setuptools import find_packages,setup
from typing import List


def get_requirements(file_name:str)->List[str]:
    '''
    this function return the list of requirements
    '''
    Hyphen_e_dot='-e .'

    with open('requirements.txt') as file_object:
        requirements=file_object.readlines()
        requirements=[req.replace('\n','') for req in requirements]
    if Hyphen_e_dot in requirements:
        requirements.remove(Hyphen_e_dot)

    return requirements






setup(
    name='mlproject',
    version='0.0.1',
    author='sourabh',
    author_email='prajapatisourabh22@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)
