import configparser

file_path = input('Please input the file path: ');

config = configparser.ConfigParser();
config.read('../data/default.config');

if not file_path:
	file_path = config['DEFAULT']['file_path'];

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
