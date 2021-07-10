import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    name="tfreecord",
    py_modules=["tfreecord", "tfrecords_pb2"],
    version="1.0",
    description="",
    author="Wikidepia",
    packages=find_packages(),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    include_package_data=True,
)
