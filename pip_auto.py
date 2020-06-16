#automate installing pip modules without using cmd every time

import os
import time

#when using for the first time, add paths to all your Python versions
PATHS = {"3.7": "---here is your path---"}

def pip_install_mod(mod_name, python_version="all", paths = PATHS):
	"""use os to install a module"""

	#to install paths --> returns list with all paths if python_version is all, else returns list with one path
	to_install_versions = []
	if python_version == "all": to_install_versions = paths.keys()
	else:
		to_install_versions = [python_version]

	_intervall_time = 1

	try:
		"""loop through all the paths and install module for each one
		   the display the path and move on to the next"""
		for current_version in to_install_versions:
			os.system(f"cd {paths[current_version]}")
			time.sleep(_intervall_time)
			os.system(f"pip install {mod_name}")
			print(f"[LOG] Package installed for Version {current_version[-3:]}\n")
			time.sleep(2)
			get_input()
	
	except Exception as e:
		print(e)
		print("[LOG] Try again")
		time.sleep(_intervall_time)
		get_input()


#In the program input the name of the module you want to download and
#the python version the module should be installed for.

#If you just leave the python version input blank, it will install for all versions defined with the paths above

def get_input():
	mod_name= input('Module: ')
	python_version = input("Python version: ")

	if python_version == "": pip_install_mod(mod_name)
	else: pip_install_mod(mod_name, python_version)

if __name__ == "__main__":
	get_input()

