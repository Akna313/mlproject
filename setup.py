from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """This function will return a list of requirements."""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # read lines from the requirements file
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('-e .')]  # clean up the lines
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    description='A machine learning project',
    author='akna',
    author_email='akna3bethmi@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
