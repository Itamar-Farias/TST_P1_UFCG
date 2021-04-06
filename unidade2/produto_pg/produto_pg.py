# coding: utf-8
# Itamar da Silva Farias	115210021
# Programação I

termo1 = int(raw_input())
termo2 = int(raw_input())
n = int(raw_input())
q = termo2 / termo1
produto_de_n = (termo1 ** n) * (q ** ((n * (n - 1) / 2)))

print produto_de_n
