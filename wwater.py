def house(n,**args):
	hour = 0
	for x in range(n):
		b = args['water'][x]/args['speed'][x]
		hour += b
	return hour

print(house(2, speed=[5,5], water=[10,20]))
