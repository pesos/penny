import urllib
import urllib2

url = 'http://pastebin.com/api/api_post.php'

def logs(phenny, input):
	text = ''
	if input == '.logs':
		num = 0
	else:
		num = int(input.split(' ')[1])
	f = open('pes-os.log', 'r')
	for line in f.readlines()[-num:]:
		text = text + line

	values = {'api_option':'paste',
          'api_dev_key':'d8a90aa1dc591a75d5beeb91fd6f7e30',
          'api_paste_code':text,
	  'api_paste_private' : '0',
	  'api_paste_format':'mirc'}

	data = urllib.urlencode(values)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	the_page = response.read()
	phenny.say(input.nick+': '+the_page)
	
logs.commands = ['logs']
logs.priority = 'medium'
