import requests

import list_process

r = requests.get('https://www.wholesomelist.com/api/list')
god_list = r.json()['table']
list_process.process(god_list)
