# coding: utf-8
# Itamar da Silva Farias	115210021	
# Programação I


def primeiro_menor(n, nums):
	for i in range(len(nums)):
		if int(nums[i]) < n:
			return i
	return -1

def main():
	seq = raw_input().split()
	num = int(raw_input())
	for j in range(len(seq)):
		seq[j] = int(seq[j])

	if primeiro_menor(num, seq) == -1:
		print "sem menores que %d" % num
	else:
		print "primeiro menor que %d: %d" % (num, seq[primeiro_menor(num, seq)])

if __name__ == "__main__":
	main()
