"""
==> For step1, Create a distribution description, we need to 
create 2 files that we 'll place in the same folder as our 
vsearch.py file. The 1st file which  must be called setup.py
describes our module in some detail.

==> the 1st line imports the setup function 
from the setuptools modulem,

==> the 2nd line invokes the setup functions.



The standard library includes a module called setuptools, which
 can be used to add any module into site-packages.

--Creating the Distribution File.
At this stage, you should have three files, which we have put in our
mymodules folder: vsearch.py, setup.py, and README.txt.
We’re now ready to create a distribution package from these files. This is Step
2 from our earlier list: Generate a distribution file. 


--When the Windows command prompt reappears, your three files have
been combined into a single distribution file. This is an installable file
that contains the source code for your module and, in this case, is called
vsearch-1.0.zip.
--You’ll find your newly created ZIP file in a folder called dist, which has also
been created by setuptools under the folder you are working in (which is
mymodules in our case).



C:/Users/Dimitrios/Desktop/myPython/mymodules> py -3 setup.py sdist


--Installing Packages with “pip”
Now that your distribution file exists as a ZIP or a tarred archive (depending on your
platform), it’s time for Step 3: Install the distribution file. As with many such things,
Python comes with the tools to make this straightforward. In particular, Python 3.4
(and newer) includes a tool called pip, which is the Package Installer for Python.


--Step 3 on Windows
Locate your newly created ZIP file under the dist folder (recall that the file is
called vsearch-1.0.zip). While in the Windows Explorer, hold down the Shift
key, then right-click your mouse to bring up a context-sensitive menu. Select Open
command window here from this menu. A new Windows command prompt opens. At this
command prompt, type this line to complete Step 3:

C:/Users/.../dist> py -3 -m pip install vsearch-1.0.zip

--The vsearch module is now installed as part of site-packages

--Modules: What We Know Already
Now that our vsearch module has been installed, we can use import vsearch
in any of our programs, safe in the knowledge that the interpreter can now find the
module’s functions when needed.
If we later decide to update any of the module’s code, we can repeat these three steps
to install any update into site-packages. If you do produce a new version of your
module, be sure to assign a new version number within the setup.py file.



!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!! WHAT WE KNOW ABOUT MODULES !!!!!

-- A module is one or more functions
saved in a file.

-- You can share a module by
ensuring it is always available with
the interpreter’s current working
directory (which is possible, but
brittle) or within the interpreter’s sitepackages
locations (by far the better
choice).

-- Following the setuptools
three-step process ensures that 
your module is installed into sitepackages,
which allows you to import the module and use its
functions no matter what your current
working directory happens to be.

!!!!!! WHAT WE KNOW ABOUT MODULES !!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
................................................................................
"""


from setuptools import setup

setup(
    	name='vsearch',
		version='1.0',
		description='The Head First Python Search Tools',
		author='HF Python 2e',
		author_email='hfpy2e@gmail.com',
		url='headfirstlabs.com',
		py_modules=['vsearch'],
	)

