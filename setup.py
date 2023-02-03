import setuptools

install_requires_list=[
    'pandas'
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_sample",
    version="0.0.1",
    description="Sample",
    package_dir={"": "src"},
    packages=setuptools.find_packages('src'),
    install_requires=install_requires_list,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wingdagger/python-sample",
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    )
)
