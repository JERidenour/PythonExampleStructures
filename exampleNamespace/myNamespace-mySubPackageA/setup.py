import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mySubPackageA",
    version="0.0.0",
    author="Jonathan Ridenour",
    description="Example build structure for python namespace package with submodules.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    test_loader="unittest:TestLoader",
    package_data={
        "mySubPackageA" : ["data/MidLevelData.json"],
        "mySubPackageA.mySubSubPackageA" : ["data/LowLevelData.json"],
        "mySubPackageA.mySubSubPackageB" : ["data/LowLevelData.json"]
    },
    include_package_data=True
)
