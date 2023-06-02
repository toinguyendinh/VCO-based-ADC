#with open('testcase_f10khz_oversample_512_fs25Mhz.txt', 'r') as input_file, open('first_data_test.txt', 'w') as output_file:

with open('../result_data/output_vco.txt', 'r') as input_file, open('first_value_ro.txt', 'w') as output_file:
	for line in input_file:
		first_value = line[0]
#		print(first_value)
		output_file.write(first_value + '\n')


#	data=file.read()
#	print(data)
