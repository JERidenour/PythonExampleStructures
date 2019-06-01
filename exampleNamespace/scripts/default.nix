with import <nixpkgs> {};
stdenv.mkDerivation rec {
  name = "env";
  env = buildEnv { name = name; paths = buildInputs; };
  buildInputs = [
    pkgs.R

    (let 
      mySubPackageA = callPackage ../myNamespace-mySubPackageA/release.nix {
        pkgs = pkgs;
        pythonPackages = python36Packages;
      };
      mySubPackageB = callPackage ../myNamespace-mySubPackageB/release.nix {
        pkgs = pkgs;
        pythonPackages = python36Packages;
      };
      in python36.withPackages (ps: [ ps.numpy ps.pandas mySubPackageA mySubPackageB ] ) 
    )

  ];
}
