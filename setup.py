from setuptools import setup

def load_description(*args):
    with open(str(args[0])) as file:
        return file.read()


NAME = "Mathly"
AUTHOR = "Aaron Ma"
VERSION = "0.1.2"
SHORT_DESCRIPTION = "Mathly is an open-source Python library for mathematics with strong Linear Algebra and Calculus support."
LONG_DESCRIPTION = load_description("README.md")

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
    packages = ["mathly"],
    classifiers = [
        "License :: OSI Approved :: MIT License",
        # "Programming Language :: Python 3.7"
    ],
    license = "MIT"
)
