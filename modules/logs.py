import urllib
import urllib2
import json

url = 'http://paste.kde.org/'

def logs(phenny, input):
	text = ''
	if input == '.logs':
		num = 0
	else:
		num = int(input.split(' ')[1])
	try:
		f = open('pes-os.log', 'r')
		for line in f.readlines()[-num:]:
			text = text + line
	except:
		phenny.say("Log file can't be read :( ")
		return
	try:
		values = {'api_submit':'true',
		  'mode':'json',
	          'paste_data':text,
		  'paste_private':'no',
		  'paste_lang':'Text'}

		data = urllib.urlencode(values)
		req = urllib2.Request(url, data)
		response = urllib2.urlopen(req)
		the_page = json.loads(response.read())
		phenny.say(input.nick+': '+'http://paste.kde.org/'+the_page['result']['id'])
	except:
		phenny.say("Can't create paste :( ")
		return
	
logs.commands = ['logs']
logs.priority = 'medium'
