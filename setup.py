from setuptools import setup, find_packages

setup(
    name="datafest-politics",
    version="0.0.1",
    description="An app from Bicoastal Datafest 2012 for parsing PDFs of congressional representitives' financial disclosures",
    author="Renee Chu and team",
    install_requires = [
        'flask',
        'simplejson',
        'sqlalchemy'
    ],
    tests_require=[
        'nose',
    ]
)