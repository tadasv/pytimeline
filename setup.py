import os
from setuptools import setup

import pytimeline

def read_file(name):
    return open(os.path.join(os.path.dirname(__file__), name)).read()


setup(
    name = "pytimeline",
    version = pytimeline.__version__,
    author = "Tadas Vilkeliskis",
    author_email = "tadas@vilkeliskis.com",
    license = "MIT",
    keywords = "mongodb timeseries",
    url = "https://github.com/tadasv/pytimeline",
    description = (
        "A layer of abstaction for storing timeseries "
        "in MongoDB."
    ),
    long_description = read_file("README.rst"),
    packages = ["pytimeline"],
)
