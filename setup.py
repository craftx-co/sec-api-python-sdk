import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sec-python-sdk",
    version="1.0.0",
    author="Parn Boonyamanee",
    author_email="parnpresso@gmail.com",
    description="Python SDK for access SEC data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/craftx-co/sec-python-sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
