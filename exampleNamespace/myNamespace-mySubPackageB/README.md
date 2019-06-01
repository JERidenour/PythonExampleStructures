Example package with submodules.

Each package contains:
- an `__init__.py`,
- a module with python code,
- a test folder with unittests for this level module,
- a data folder with a `.json` file to support the module.

Tests are run on build.

Data is included in the build and can be accessed using the `pkg_resources` api.
