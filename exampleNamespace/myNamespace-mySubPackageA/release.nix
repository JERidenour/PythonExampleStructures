{ lib, pkgs, pythonPackages }:

with pkgs;

pythonPackages.buildPythonPackage rec {
  pname = "mySubPackageA";
  version = "0.0.0";

  src = ./.;

  propagatedBuildInputs = [ pythonPackages.numpy pythonPackages.pandas ];
}
