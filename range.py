st = input('Input start of the range\n')
end = int(input('Input end of the range\n'))
step = input('Input step\n')
if step:
	step = int(step)
else:
	step = 0
if st:
	st = int(st)
else:
	st = 0
def range_(st, end, step):
	i = st
	while st <= i <= end:
		if step > 0:
			print (i)
			i += step
		elif step < 0:
			i = end
			print (i)
			end += step
			i = end
		else:
			print (i)
			i += 1
range_(st, end, step)