from typing import List

from setuptools import find_packages, setup

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
    install_requires=['psycopg2-binary', 'mysql-connector-python', 'pymongo', 'pymongo[srv]', 'dnspython', 'ensure', 'pytest==7.1.3', 'tox', 'black==22.8.0', 'flake8==5.0.4', 'mypy==0.971']
    )


