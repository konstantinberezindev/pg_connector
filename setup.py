from setuptools import setup, find_packages


setup(
    name="pg_connector",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "asyncpg==0.29.0"
    ],
)
