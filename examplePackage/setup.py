import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="myPackage",
    version="0.0.0",
    author="Jonathan Ridenour",
    description="Example build structure for python package with submodules.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    test_loader="unittest:TestLoader",
    package_data={
        "myPackage" : ["data/TopLevelData.json"],
        "myPackage.mySubPackageA" : ["data/MidLevelData.json"],
        "myPackage.mySubPackageB" : ["data/MidLevelData.json"],
        "myPackage.mySubPackageA.mySubSubPackageA" : ["data/LowLevelData.json"],
        "myPackage.mySubPackageA.mySubSubPackageB" : ["data/LowLevelData.json"]
    },
    include_package_data=True
)
