#PLA.py
import numpy as np
import math
import random
import sys

def sign_CL(wx):
	if (wx > 0):
		return 1
	else:
		return -1

wieght = [0, 0, 0, 0, 0]
# print wieght[0], wieght[1], wieght[2], wieght[3], wieght[4]
# print np.sign([-5., 4.5, 0])

from random import shuffle
x = [[i] for i in range(400)]
shuffle(x)


input_data = open("PLA_data.txt", "r+") # input_data
line = input_data.readlines() # load data into python
lenght = len(line)    # get how many data had being loaded 
# print lenght
print ""
counter = 0
while_counter = 1
# print element[0], element[1],element[2], elemrnt1[0], elemrnt2[0]
occur_counter = 0
pre_occur_counter = -1
occur_counter_sum = 0
# print wieght[0], wieght[1], wieght[2], wieght[3]
# for outer_index in range(0, 5, 1):
run_time = 2000
for index_out in range(0, run_time, 1):
	x = [[i] for i in range(400)]
	shuffle(x)
	wieght = [0, 0, 0, 0, 0]
	stop = 0
	outer_index = 0
	pre_occur_counter = -1
	occur_counter = 0
	while (stop != 1):
		# print "outer_index=", outer_index
		pre_occur_counter = occur_counter
		for index in range(0, lenght, 1):
			element = line[int(x[index][0])].split(' ')
			elemrnt1 = element[3].split('\t')
			elemrnt2 = elemrnt1[1].split('\n')
			WX = float(element[0]) * float(wieght[0]) + float(element[1]) * float(wieght[1]) + float(element[2]) * float(wieght[2]) + float(elemrnt1[0])* float(wieght[3]) + float(wieght[4]) 
			if(sign_CL(WX) * int(elemrnt2[0]) < 0):
				wieght[0] = wieght[0] + float(element[0]) * float(elemrnt2[0]) * 0.5  #1 #
				wieght[1] = wieght[1] + float(element[1]) * float(elemrnt2[0]) * 0.5
				wieght[2] = wieght[2] + float(element[2]) * float(elemrnt2[0]) * 0.5
				wieght[3] = wieght[3] + float(elemrnt1[0])* float(elemrnt2[0]) * 0.5
				wieght[4] = wieght[4] + 1* float(elemrnt2[0]) * 0.5
				occur_counter += 1
				# print wieght[0], wieght[1], wieght[2], wieght[3]
		if (pre_occur_counter == occur_counter):
			stop = 1
		
		outer_index +=1
	occur_counter_sum = occur_counter_sum + occur_counter
		
	# print "occur_counter=", occur_counter
print occur_counter_sum / float(run_time)

