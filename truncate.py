line_number = 50000
infile = 'latest-all.json'
outfile = 'truncate' + str(line_number) + '.json'
with open(infile, 'r') as f1, open(outfile, 'w') as f2:
	for i in range(line_number):
		if i % 1000 == 0:
			print(i)
		line = f1.readline()
		if i != line_number - 1:
			f2.writelines(line)
		else:
			# truncate the last two characters: return and ','
			f2.writelines(line[:-2])
	f2.writelines(']')