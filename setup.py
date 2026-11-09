from setuptools import find_packages, setup

setup(
    name="analyzer",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "emd-signal",
        "pandas",
        "matplotlib",
        "openpyxl",
        "python-dotenv",
        "pingouin",
    ],
    extras_require={
        "conda": ["pypdf2"],
        "pip": ["neuronol"],
    },  # this does not install, only documents
)

# Install using: `pip install -e .`
# For the extras:
# pip install -e ".[pip]"
# pip install -e ".[conda]"
