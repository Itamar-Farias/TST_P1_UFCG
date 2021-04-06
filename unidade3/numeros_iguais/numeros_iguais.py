# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

num_1 = int(raw_input())
num_2 = int(raw_input())
num_3 = int(raw_input())

if num_1 == num_2  and num_1 == num_3 and num_2 == num_3:
	print 3
elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
	print 2
else:
	print 0
