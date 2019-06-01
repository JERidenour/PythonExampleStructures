with import <nixpkgs> {};
stdenv.mkDerivation rec {
  name = "env";
  env = buildEnv { name = name; paths = buildInputs; };
  buildInputs = [
    pkgs.R

    (let 
      myPackage = callPackage ../release.nix {
        pkgs = pkgs;
        pythonPackages = python36Packages;
      };
      in python36.withPackages (ps: [ ps.numpy ps.pandas myPackage ] ) 
    )

  ];
}
