from setuptools import find_packages,setup
from typing import List
HAN_E="-e."

def get_requirement(file_path:str)->List[str]:
    requirements=[]
    with open(file_path)as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n",'') for req in requirements]
        if HAN_E in requirements:
            requirements.remove(HAN_E)
    return requirements

setup(
    name="customer_churn_prediction",
    version='0.0.1',
    author="Nivetha",
    package=find_packages(),
    instal_requires=get_requirement("requirements.txt")
)
