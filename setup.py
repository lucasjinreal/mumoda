import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    name="mumoda",
    py_modules=["mumoda"],
    version="0.1",
    description="",
    author="Lucas Jin",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    include_package_data=True,
    extras_require={"dev": ["pytest"]},
)
