import os
import os.path


def list_files(path):
	'''List all the files in the given directory'''
	files = [];
	for f in os.listdir(path):
		file_path = os.path.join(path, f);
		if not f.startswith('.'):
			if os.path.isfile(file_path):
				files.append(f)
			elif os.path.isdir(file_path):
				files.extend(list_files(file_path))

	return files;

path = input('Please input the root directory: '); # /Users/neo/Documents/projects/python
files = list_files(path);

print(files);
