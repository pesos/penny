def logs(phenny, input):
	f = open('/home/phalgun/coding/example.log', 'r')
	for line in f:
		phenny.say(line)

logs.rule = r'$nickname: logs!'
logs.priority = 'medium'
logs.thread = False
