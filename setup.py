from setuptools import setup, find_packages


setup(
    name="pg_connector",
    description='Simple python library to work with asyncpg',
    author='Konstantin Berezin',
    author_email='mrkonstantinberezin@gmail.com',
    version="0.2",
    packages=find_packages(),
    install_requires=[
        "asyncpg==0.29.0",
        "python-dotenv==1.0.1"
    ],
)
