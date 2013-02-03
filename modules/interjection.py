from time import gmtime, strftime
import logging
import os

if os.path.exists('pes-os.log') is False:
	f = open('pes-os.log','a')
	f.close()

logging.basicConfig(filename='pes-os.log', format='[%(asctime)s]%(message)s', datefmt='%d/%m/%Y %I:%M:%S', level=logging.INFO)

def interjection(phenny, input):
        logging.info(' <'+input.nick+'> '+input)

interjection.rule = r'.*'
interjection.priority = 'high'
interjection.thread = False
