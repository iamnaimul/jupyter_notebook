# Import Subprocess and Os module
import subprocess
import os

def run_jupyter():
	url = 'D:\DOCUMENTS STORE\offline_PYTHON'
	os.chdir(url)
	subprocess.getoutput('jupyter notebook')


run_jupyter()
print('Do Not Close The Window\nPress Quite on Browser\nthen Close it')
