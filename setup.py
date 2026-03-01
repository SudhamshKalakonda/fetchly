from setuptools import setup, find_packages

setup(
    name="fetchly",
    version="0.1.0",
    author="Sudhamsh Kalaonda",
    author_email="sudhamshguptha14@gmail.com",
    description="A lightweight Python HTTP library with retries, timeouts, and automatic headers",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    python_requires=">=3.6",
)