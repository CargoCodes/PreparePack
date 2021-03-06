# PreparePack

Repository that prepares directories and files for programming and uploading Python packages.

`Installation:`

    $ pip install preparepack

`Usage:`

    $ prepack packageName

Replace packageName with the name of your package. 
It will create the package directory named "packageName_package",
the "setup.py" file, a subdirectory named "packageName" containing 
the ___init_ __.py file and the package file named "packageName.py" .

    $ buildpack 

Using this command you build the needed files before uploading your repository, such as .tar.gz and .whl .
When you use this command, you must be in the same directory where the setup.py file is located.

    $ uploadpypi

Calling this command, you start the procedure for uploading a package on Pypi. 
Make sure to be in the the directory which contains the dist folder.
Make also sure to have a valid Pypi account, to remember the credentials and that your package 
has a valid name (not taken yet) and a valid version (not uploaded yet).

All commands have "--help" option.
