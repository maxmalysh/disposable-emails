from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='disposable-emails',
    version='1.0.0',
    author='Max Malysh',
    author_email='github@maxmalysh.com',
    url='https://github.com/maxmalysh/disposable-emails',
    description='Weed out disposable email providers with ease',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Topic :: Communications :: Email",
    ],
)
