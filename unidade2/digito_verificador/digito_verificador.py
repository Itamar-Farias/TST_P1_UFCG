# coding: utf-8
# Itamar da SIlva Farias	115210021
# Programação I

conta = raw_input()
dv = (float(conta[0]) + float(conta[1]) + float(conta[2]) + float(conta[3]) + float(conta[4])) % 11
if dv >= 10:
	print "%s-%d" % (conta, dv)
else:
	print "%s-0%d" % (conta, dv)
