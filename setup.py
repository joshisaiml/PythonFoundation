from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements


setup(
    name="mlproject",  # Package name
    version="0.1.0",   # Start with 0.1.0 and increment as you release
    author="Shweta Joshi",
    author_email="joshis@ussilica.com",
    description="A sample machine learning project - Python Foundations Food Hub",
    long_description=open("README.md").read(),  # falls back to README.md
    long_description_content_type="text/markdown",
    url="https://github.com/joshisaiml/PythonFoundation",
    packages=find_packages(),   # Automatically finds packages in your folder
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Or the license you prefer
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=get_requirements('requirement.txt')
)
