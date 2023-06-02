import numpy as np
with open("pha_vco_primary.txt", "r") as txt_file:
        input_data = [list(map(str, line.split())) for line in txt_file];
txt_file.close()
clk = [row[0] for row in input_data]
clk = list(map(int, clk))
output_data = []
for i in range(0, len(clk)-1):
        if clk[i] > clk[i+1]:
                output_data.append(input_data[i+1])
output_data_np = np.asarray(output_data,dtype=np.float32)

idx = output_data_np>=1.75
not_idx = output_data_np<1.75

output_data_np[idx]=1
output_data_np[not_idx]=0

output_data = np.delete(output_data_np, 0, 1)

np.savetxt("pha_vco_output_data.txt", output_data, fmt='%d', delimiter='', newline='\n')

#print(type(output_data_np))

sum_data = np.sum(output_data_np, axis=1, dtype=int)
np.savetxt("pha_vco_sum_data.txt", sum_data, fmt='%d')


