"""
SOS!!! HOW ARE MODULES FOUND??...
1. Your current working directory
This is the folder that the interpreter thinks you are currently
working in.

2. Your interpreter’s site-packages locations
These are the directories that contain any third-party Python
modules you may have installed (including any written by you).

3. The standard library locations
These are the directories that contains all the modules that make up
the standard library.



However, adding or removing modules to your site-packages locations is positively encouraged, so
much so that Python comes with some tools to make it straightforward.


Using “setuptools” to install into site-packages

As of release 3.4 of Python, the standard library includes a module called
setuptools, which can be used to add any module into site-packages.
Although the details of module distribution can—initially—appear complex,
all we want to do here is install vsearch into site-packages, which is
something setuptools is more than capable of doing in three steps:

1. Create a distribution description
This identifies the module we want setuptools to install.

2. Generate a distribution file
Using Python at the command line, we’ll create a shareable
distribution file to contain our module’s code.

3. Install the distribution file
Again, using Python at the command line, install the distribution
file (which includes our module) into site-packages.


"""


def search4letters(phrase:str, letters:str = "aeiou") -> set:
	"""Return a set of the "letters" found in "phrase."""
	return set(letters).intersection(set(phrase))

def search4vowels(phrase:str,) -> set:
	"""Return any vowels found in a supplied phrase."""
	vowels = set("aeiou")
	return vowels.intersection(set(phrase))