# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

m = int(raw_input())
n = int(raw_input())

while not n == 0:
	resto = m % n
	m = n
	n = resto

print m
