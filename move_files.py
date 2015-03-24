import os
import os.path
import shutil

def list_files(root_directory):
	'''List all the files in the given directory'''
	files = [];
	for f in os.listdir(root_directory):
		file_path = os.path.join(root_directory, f);
		if not f.startswith('.'):
			if os.path.isfile(file_path):
				files.append(file_path);
			elif os.path.isdir(file_path):
				files.extend(list_files(file_path));

	return files;

def move_files(destination_directory, files, is_copy = True):
	new_files = [];
	for f in files:
		destination_path = os.path.join(destination_directory, os.path.basename(f));
		new_files.append(destination_path);
		if is_copy:
			shutil.copyfile(f, destination_path);
		else:
			shutil.move(f, destination_path);

	return new_files;

root_directory = input('Please input the root directory: '); # /Users/neo/Documents/projects/python
destination_directory = input('Please input the destination directory: '); # /Users/neo/Documents/projects/test

if not os.path.exists(destination_directory):
	os.makedirs(destination_directory);

files = list_files(root_directory);
files = move_files(destination_directory, files, False);

print(files);
