# Import Subprocess and Os module
import subprocess
import os

def run_jupyter():
	url = 'D:\DOCUMENTS STORE\offline_PYTHON'
	os.chdir(url)
	subprocess.getoutput('jupyter notebook')


run_jupyter()
