import os.path
import sys

import setuptools

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "spoken2written"))

with open("README.md", encoding="utf8") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

with open("requirements.txt") as f:
    reqs = f.read()

DISTNAME = "spoken2written"
DESCRIPTION = "spoken2written: a short library to convert spoken english transcipts to written english."
LONG_DESCRIPTION = readme
AUTHOR = "Suhruth Eedara"
LICENSE = license
REQUIREMENTS = (reqs.strip().split("\n"),)

if __name__ == "__main__":
    setuptools.setup(
        name=DISTNAME,
        install_requires=REQUIREMENTS,
        packages=setuptools.find_packages(),
        version="0.1",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        author=AUTHOR,
        license=LICENSE,
        classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
    )
