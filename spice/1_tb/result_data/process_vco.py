import numpy as np

#read file text
with open ("vco_data.txt", "r") as input_file:
	input_data = [list(map(str, line.split())) for line in input_file];
input_file.close()

#print(input_data)

output_data_np = np.asarray(input_data, dtype=np.float32)
#print(output_data_np)

idx = output_data_np >= 1.7
not_idx = output_data_np < 1.7

output_data_np[idx] = 1
output_data_np[not_idx] = 0

#output_data = np.delete(output_data_np, 0, 1)
#print(output_data)

np.savetxt("output_vco.txt", output_data_np, fmt='%d', delimiter='', newline='\n')

#first value
#for line in output_data: 
#	first_value = line[0]
#	print(first_value)
#	output_file.write(first_value + '\n')
#	np.savetxt()

