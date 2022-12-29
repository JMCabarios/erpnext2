from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in jmcustomapp/__init__.py
from jmcustomapp import __version__ as version

setup(
	name="jmcustomapp",
	version=version,
	description="custom app",
	author="jm",
	author_email="janmaricabarios@yahoo,com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
