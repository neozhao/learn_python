import os
import os.path
import shutil
import time
import configparser

def list_directories(root_directory, file_types = [], created_time = None):
	'''List all the directories in the given directory, filter by filter_types and created_time if provided'''
	for f in os.listdir(root_directory):
		path = os.path.join(root_directory, f);
		ext = os.path.splitext(f)[1][1:].lower();
		if not f.startswith('.'):
			if os.path.isfile(path):
				if not file_types or ext in file_types:
					print(f + ', type: ' + ext + ', created at: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.stat(path).st_ctime)));
			if os.path.isdir(path):
				list_directories(path, file_types, created_time);
			

root_directory = input('Please input the root directory: ');

config = configparser.ConfigParser();
config.read('../data/default.config');

if not root_directory:
	root_directory = config['DEFAULT']['root_directory'];

list_directories(root_directory, ['jpg']);
