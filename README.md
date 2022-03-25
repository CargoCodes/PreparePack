# PreparePack

Repository that prepares packages directories and files

Installation:

    $ pip install preparepack

Usage:

    $ prepack packageName

Replace packageName with the name of your package.
It will create the package directory named aspackageName_package, the setup.py file,
a subdirectory named packageName containing the __ init __.py file and the package file named as packageName.py .

    $ buildpack 

Using this command you build the needed files before uploading your repository, such as .tar.gz and .whl .
When you use this command, you must be in the same directory where the setup.py file is located.

    $ uploadpypi

Calling this command, you start the procedure for uploading a package on Pypi.
Make sure to be in the the directory which contains the dist folder.
Make also sure to have a valid Pypi account, to remember the credentials and that your package
has a valid name (not taken yet) and a valid version (not uploaded yet).
