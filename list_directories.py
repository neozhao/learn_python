import os
import os.path
import shutil
import time

def list_directories(root_directory):
	'''List all the directories in the given directory'''
	for f in os.listdir(root_directory):
		path = os.path.join(root_directory, f);
		if os.path.isdir(path):
			# print(f + ' created at ' + time.strftime("%Y%m%d% H%M%S", os.stat(path).st_ctime));
			# print(os.stat(path).st_ctime.strftime("%Y%m%d% H%M%S"));
			print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.stat(path).st_ctime)));

root_directory = input('Please input the root directory: '); # /Users/neo/Documents/projects/python

list_directories(root_directory);
