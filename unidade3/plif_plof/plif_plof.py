num_1 = int(raw_input())
num_2 = int(raw_input())
num_3 = int(raw_input())

soma = num_1 + num_2 + num_3

if soma % 3 == 0 and soma % 5 == 0:
	print "plifplof"
elif soma % 3 == 0:
	print "plif"
elif soma % 5 == 0:
	print "plof"
else:
	print soma
