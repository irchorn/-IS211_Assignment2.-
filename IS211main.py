


def downloadData(url):
    return url


import urllib.request

with urllib.request.urlopen('http://python.org/') as response:
    html = response.read()


def processData(file):
    for line in file:
        return person_bd
    person_bd = {ID: (name, birthday)}


import datetime

birthday = datetime.date.strptime('%m/%d/%Y').date()
print(birthday)


import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
