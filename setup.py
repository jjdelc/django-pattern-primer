from setuptools import setup, find_packages

setup(

    name = "django-pattern-primer",

    version = "0.0.1",

    packages = find_packages(),

    install_requires = ['Django>=1.2.3'],
    include_package_data = True,

    # metadata for upload to PyPI
    author = "Jj Del Carpio",
    author_email = "jjdelcr@gmail.com",
    description = "Pattern primer for Django",
    license = "MIT License",
    keywords = "css django pattern html",
    url = "https://github.com/jjdelc/django-pattern-primer",

)
