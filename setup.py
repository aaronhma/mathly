# from distutils.core import setup
from setuptools import setup
# from .mathly.shared import version

def load_description(readme="README.md"):
    with open(readme) as file:
        return file.read()


NAME = "Mathly"
AUTHOR = "Aaron Ma"
# VERSION = version.VERSION
VERSION = "0.1.2"
SHORT_DESCRIPTION = "Mathly is an open-source Python library for mathematics with strong Linear Algebra support."
LONG_DESCRIPTION = load_description()

setup(
    name = NAME,
    version = VERSION,
    author = AUTHOR,
    description = SHORT_DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    long_description_content_type = "text/markdown",
    url = "https://github.com/aaronhma/mathly",
    keywords = ["math", "linear algebra", "mathly"],
    include_package_data = True,
    classifiers = [
        "License :: OSI Approved :: MIT License",
        # "Programming Language :: Python 3.7"
    ],
    license = "MIT"
)
