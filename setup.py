from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return the list of requirements
    """

    requirement_lst:List[str] = []

    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            # Process each line
            for line in lines:
                requirements = line.strip()
                # ignore empty lines and -e.
                if requirements and requirements != "-e .":
                    requirement_lst.append(requirements)
    
    except FileNotFoundError:
        print("Error: The file requirements.txt was not found.")

    return requirement_lst

print(get_requirements())

setup(
    name="Network Security System",
    version="0.0.1",
    author="Arka Samanta",
    author_email="arkasamanta04@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)