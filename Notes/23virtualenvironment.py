# A virtual environment is a tool used to isolate specific Python environments on a single machine, 
# allowing you to work on multiple projects with different dependencies and packages without conflicts. 
# This can be especially useful when working on projects that have conflicting package versions or packages 
# that are not compatible with each other.

# Create a virtual environment
python -m venv myenv ( for Linux and Windows )
python3 -m venv myenv ( for macOS )

# Activate the virtual environment (Linux/macOS)
source myenv/bin/activate

# Activate the virtual environment (Windows)
myenv\Scripts\activate.bat

# Activate the virtual environment (PowerShell)
.\myenv\Scripts\activate.ps1    

# Deactivate the virtual environment
deactivate

# Install packages in the virtual environment
pip install package_name    

# Uninstall packages in the virtual environment
pip uninstall package_name

# List all packages installed in the virtual environment
pip list

# Install packages globally
pip install --user package_name

# Uninstall packages globally
pip uninstall --user package_name    

# List all packages installed globally
pip list --user

# Install packages in the virtual environment without installing them globally
pip install --no-user package_name

# Uninstall packages in the virtual environment without uninstalling them globally
pip uninstall --no-user package_name


#  The "requirements.txt" file

# Output the list of installed packages and their versions to a file
pip freeze > requirements.txt

# To install the packages listed in the requirements.txt file, 
# you can use the pip install command with the -r flag:

# Install the packages listed in the requirements.txt file
pip install -r requirements.txt

# Using a virtual environment and a requirements.txt file 
# can help you manage the dependencies for your Python projects 
# and ensure that your projects are portable and can be easily set up on a new machine.

# To check the version installed in the code editor

import pandas as pd
print(pd.__version__)