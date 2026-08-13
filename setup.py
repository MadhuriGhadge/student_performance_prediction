# responsible for building the whole machine learning project as a package and installing it in the environment

from setuptools import setup, find_packages

HYPEN_E_DOT = '-e .'

def get_requirements(file_path):
    with open(file_path, 'r') as f:
        requirements = f.read().splitlines()
        requirements = [req for req in requirements if req.strip() and not req.startswith('#')]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

    
setup(
    name='src',
    version='0.1.0',
    packages=find_packages(),
    author = 'Madhuri',
    install_requires=get_requirements('requirements.txt'),
    entry_points={
        'console_scripts': [
            'train = src.pipeline.train_pipeline:main',
            'predict = src.pipeline.predict_pipeline:main'
        ]
    }
)