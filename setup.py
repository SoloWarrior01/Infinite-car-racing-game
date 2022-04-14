import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='on the run',
    version='1.0.0',
    author='Vaibhav Bansal',
    author_email='vaibhavbansal1998@gmail.com',
    license='MIT',
    description='This is a simple game',
    long_description= long_description,
    long_description_content_type="text/markdown",
    url="mypackage.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
