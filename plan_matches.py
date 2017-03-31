import collections
import sys
filename = str(sys.argv[1])

tu = [[]]
with open(filename) as f:
	a,b = f.readline().split()
	if a < b:
		match = '(' + a + ', '+  b+ ')'
	else: 
		match = '(' + b + ', '+  a+ ')'
	tu[0].append(match + ' ' + str(0))
	for line in f:
		a, b = line.split()
		if a < b:
			match = '(' + a + ', '+  b+ ')'
		else: 
			match = '(' + b + ', '+  a+ ')'

		x = 0 
		while x <len(tu):
			flag = 1
			flagg = 0
		
			for y in range(0,len(tu[x])):
				if a in tu[x][y] or b in tu[x][y]:
					flag = 0
			if flag is 1:
				tu[x].append(match + ' ' + str(x))
				flagg = 1
				break;
			else:
				x+=1
		if flagg is 0:
			tu.append([match + ' ' + str(x)])
	
		
output = []
for x in tu:
	for y in x:
		output.append(y)
		
output = sorted(output)
for x in range(0, len(output)):
	print(''.join(output[x]))	
	