from setuptools import setup
from mathly.shared import version


def load_description(readme="README.md"):
    with open(readme) as file:
        file.open()


NAME = "Mathly"
AUTHOR = "Aaron Ma"
VERSION = version.VERSION
SHORT_DESCRIPTION = "Mathly is an open-source Python library for mathematics with strong Linear Algebra support."
LONG_DESCRIPTION = load_description()

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR, description=SHORT_DESCRIPTION, long_description=LONG_DESCRIPTION, long_description_content_type="text/markdown",
    url="https://github.com/aaronhma/mathly", keywords=["math", "linear algebra", "mathly"], license="MIT")
