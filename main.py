# Import Subprocess and Os module
import subprocess
import os

def run_jupyter():
	url = 'D:\DOCUMENTS STORE\offline_PYTHON'
	os.chdir(url)
	subprocess.getoutput('jupyter notebook')


print('************************\nDO NOT CLOSE THIS WINDOW\n************************\nPress Quit on Browser\nthen Close it\nThank You')
run_jupyter()
