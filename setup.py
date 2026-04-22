from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]

        # 🔥 REMOVE '-e .'
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='ml_project',
    version='0.1',
    packages=find_packages(),
    author_email='vipin20mar@gmail.com',
    install_requires=get_requirements('requirements.txt')
)