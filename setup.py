import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "cnnClassifier"
AUTHOR_USER_NAME = "Ashwinee"
SRC_REPO = "cnnClassifier"

setuptools.setup(
    name="cnnClassifier",
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="A simple CNN classifier for image classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/satyarth/cnnClassifier",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)