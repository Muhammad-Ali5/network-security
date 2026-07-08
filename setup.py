"""
    the setup.py file is used to package and distribute the networksecurity module. It contains metadata about the module, such as its name, version, author, 
    and dependencies. This file is essential for installing the module using pip or other package managers.

"""

from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirement_list: List[str] = []
    try: 
        with open("requirements.txt") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    return requirement_list

# print(get_requirements("requirements.txt"))
setup(
    name="networksecurity",
    version="0.0.1",
    author="Muhammad Ali",
    author_email="maliuetm507@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)