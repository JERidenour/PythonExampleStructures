import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mySubPackageB",
    version="0.0.0",
    author="Jonathan Ridenour",
    description="Example build structure for python namespace package with submodules.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    test_loader="unittest:TestLoader",
    package_data={
        "mySubPackageB" : ["data/MidLevelData.json"]
    },
    include_package_data=True
)
