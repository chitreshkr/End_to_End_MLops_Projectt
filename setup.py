import setuptools

with open("README.md",'r',encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "END-TO-END-MLOPS-PROJECT"
AUTHOR_USERNAME = "CHITRESHKR"
SRC_REPO = "MLOps_project"


setuptools.setup(
    name = SRC_REPO,
    version= __version__,
    author= AUTHOR_USERNAME,
    description= "a small python package for MLOps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls ={
        "Bug Tracker" : f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues",
        
    },
    package_dir= {"":"src"},
    packages= setuptools.find_packages(where='src')
)