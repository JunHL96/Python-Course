# main.py

# Importing the entire 'app' module to use its functions and variables.
# A module in Python is simply a file that contains Python definitions and statements.
# The 'app.py' file is acting as a module that we can import here.
# When you import a module, Python executes the code in that module and makes its functions/variables accessible.
import app

# The 'roll_dice' function is defined in the 'app' module.
# By importing 'app', we can access its functions using the 'app.<function_name>' syntax.
# In this case, 'app.roll_dice(10)' calls the roll_dice function with 10 as an argument,
# which returns a random integer between 1 and 10 (both inclusive).
# The result is printed out.
print(app.roll_dice(10))

# Python Documentation:
# For more details about Python's built-in and external modules, check the Python module index:
# https://docs.python.org/3/py-modindex.html

# Note on Built-in Modules:
# Built-in modules are part of the Python standard library. They come pre-installed with Python,
# so you can use them without installing anything extra. Examples include 'math', 'os', and 'random'.
# These modules are highly optimized for performance and are cross-platform.

# External Modules:
# External modules are not included with Python by default. They need to be installed separately.
# These are typically downloaded from the Python Package Index (PyPI) using 'pip', which is Python's package manager.
# Once installed, external modules are stored in the 'site-packages' directory,
# which is part of your Python environment on your computer.

# Notes on pip:
# 'pip' stands for "Pip Installs Packages" and is the official package installer for Python.
# It allows you to install, update, and manage external modules and libraries from PyPI.
# For example, to install the external module 'pylatex', you would run the following command in your terminal:
# pip install pylatex

# Some useful pip commands:
# 'pip install <package_name>' - Installs a package (e.g., pip install numpy)
# 'pip list' - Lists all the installed Python packages in your environment
# 'pip uninstall <package_name>' - Uninstalls a package
# 'pip install --upgrade <package_name>' - Upgrades a package to the latest version

# External modules are stored in a directory known as 'site-packages' on your machine.
# This location can vary depending on the operating system and Python environment.
# On macOS, for example, the site-packages folder can typically be found under:
# /Library/Frameworks/Python.framework/Versions/3.x/lib/python3.x/site-packages/