from distutils.core import setup
from setuptools import find_packages

setup(
  name="Pluudie",  
  version="0.0.1",
  description="A tool for food",
  author="Kasper Kloster",
  author_email='kasperkloster@gmail.com',
  url="https://github.com/KasperKloster/Pluudie",
  python_requires='>=3, <4', 
  package_dir = {'' : 'src'}, 
  packages=find_packages(),
  install_requires=[
    'gspread >= 5.6.2', 
    'firebase_admin >= 6.0.1', 
    'pandas >= 1.5.1',    
  ],

  entry_points={
        'console_scripts': [
            'p-cli = main:Main',
        ]
    }
)