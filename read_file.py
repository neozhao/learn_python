file_path = input('Please input the file path: '); # /Users/neo/Documents/projects/test/text.txt

try:
	data = open(file_path);

	for line in data:
		print(line);

	data.close();
except:
	print('exception');
	raise;
	#pass;
else:
	print('else');
	pass;
finally:
	print('finally');
	pass;
