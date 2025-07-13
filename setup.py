from setuptools import setup, find_packages

# Read requirements.txt file
with open('requirements.txt')as f:
    requirements = f.read().splitlines()

setup(
    name='MLOPS-PROJECT-1',
    version= "0.1",
    author='Pooja',
    packages=find_packages(), # it will automatically detect all packages (utils, src, config)
    install_requires = requirements,
)