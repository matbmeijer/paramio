import os
import re

from setuptools import setup

root = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(root, "paramio", "__init__.py"), "r") as init_file:
    init_content = init_file.read()

attrs = dict(re.findall(r"__([a-z]+)__ *= *['\"](.+)['\"]", init_content))

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="python-box",
    version=attrs["version"],
    url="https://github.com/matbmeijer/paramio",
    license="MIT",
    author=attrs["author"],
    install_requires=[],
    author_email="matthias@brennotten.net",
    description="Define dynamic parameters only once",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["paramio"],
    packages=["paramio"],
    python_requires=">=3.7",
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
