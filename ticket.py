ticketno = list(input('Input ticket number\n'))
for i in range(len(ticketno)):
	ticketno[i] = int(ticketno[i])
def success(t):
	l = len(t) // 2
	if l:
		pass
	else:
		print('Ticket number must be even')

	if sum(t[0:l]) == sum(t[l:]):
		print('success')
	else:
		print('fail')
success(ticketno)