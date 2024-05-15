from typing import List

from setuptools import find_packages, setup

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str) -> List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()     
   
__version__ = "0.0.1"
REPO_NAME = "DBGenie"
PKG_NAME= "dbgenie"
AUTHOR_USER_NAME = "hrshankar2002"
AUTHOR_EMAIL = "hrshankar2002@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for automating database operations.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements('./requirements_dev.txt'),
    )

