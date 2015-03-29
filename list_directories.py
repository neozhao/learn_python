import os
import os.path
import shutil
import time
import datetime
import configparser

def list_directories(root_directory, file_types = [], start_time = None):
	'''List all the directories in the given directory, filter by filter_types and start_time if provided'''
	for f in os.listdir(root_directory):
		path = os.path.join(root_directory, f);
		ext = os.path.splitext(f)[1][1:].lower();
		created_time = os.stat(path).st_ctime;

		if not f.startswith('.'):
			if os.path.isfile(path):
				if (not file_types or ext in file_types) and (not start_time or created_time > start_time):
					print(f + ', type: ' + ext + ', created at: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(created_time)));
			if os.path.isdir(path):
				list_directories(path, file_types, start_time);
			

root_directory = input('Please input the root directory: ');

config = configparser.ConfigParser();
config.read('../data/default.config');

if not root_directory:
	root_directory = config['DEFAULT']['root_directory'];

list_directories(root_directory, ['jpb'], datetime.datetime(2015, 3, 20).timestamp());
# list_directories(root_directory, ['jpg']);
# list_directories(root_directory, [], datetime.datetime(2015, 3, 20).timestamp());
