from time import gmtime, strftime
import logging

logging.basicConfig(filename='/home/phalgun/coding/example.log', format='%(asctime)s:%(message)s', datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.INFO)

def interjection(phenny, input):
        logging.info(' '+input.nick+': '+input)

interjection.rule = r'.*'
interjection.priority = 'high'
interjection.thread = False
