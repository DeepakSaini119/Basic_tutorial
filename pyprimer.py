#command line arguments
import sys
output_file = sys.argv[1]

#I/O 
file_handler_out = open(output_file,'w')
for i in range(10):
	cur_str = str(i)+','+str(i+1)+','+str(i+2)+'\n'
	file_handler_out.write(cur_str)
file_handler_out.close()

file_handler_in = open(output_file)
vec = file_handler_in.readlines() 

#list comprehension
vec = [ele.strip().split(',') for ele in vec]
vec = [[int(ele) for ele in sub_vec] for sub_vec in vec]

print vec
file_handler_in.close()

# sys.exit()



