def dec(position):
	w = 'white'
	b = 'black'
	white = ['a','c','e', 'g']
	black = ['b','d','f', 'h']
	pair = [w,b,w,b,w,b,w,b]
	not_pair = [b,w,b,w,b,w,b,w]
	first=position[0]
	second=position[1]
	if first in white:
		if int(second) % 2:
			return b
		else:
			return w
	if first in black:
		if int(second) % 2:
			return w
		else:
			return b

def find_slon(pos1, pos2):
	s = dec(pos1)
	f = dec(pos2)
	if s == f:
		return 'Yes'
	else:
		return 'No'

print(find_slon('f5', 'd4'))
