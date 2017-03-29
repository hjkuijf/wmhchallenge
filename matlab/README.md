# From matlab to Docker
This example shows you how to compile your matlab script for Docker. Full details are given here: http://wmh.isi.uu.nl/methods/example-matlab/ This example uses matlab R2016a on CentOS 7 64-bit.

## The source
The script is located in src/example.m and needs the nifti toolbox located in the src/nifti-folder.

## Compilation
In matlab, open the Application Compiler. Add you main file (example.m) and all other files that are needed to run (in this case the nifti-folder). The output of the compiler is located in the folder bin.

## Compiler output
The compiler output is located in the folder bin. For participation in the challenge, only the folder bin/for_redistribution_files_only is actually needed.
