from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='is-numeric',
      version='1.0.0',
      author='Mighty Pulpo',
      author_email='jayray.net@gmail.com',
      description='The missing Python method to determine if a value is numeric',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=find_packages(),
      classifiers=[
          'Programming Language :: Python :: 3',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
      ],
      python_requires='>=3.6',
      keywords='isnumeric, is_numeric, number, isnumber, is_number, "is numeric", "is number", numeric')
