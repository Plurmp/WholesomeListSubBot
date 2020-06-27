import requests
import time

import new_entry_detection
import list_process

api = "https://wholesomelist.com/api/list"


def main():
    r = requests.get(api)
    local_list = r.json()['table']
    while True:
        god_list = r.json()['table']
        new_entry_detection.check_new_entry(god_list, local_list)
        list_process.process(god_list)
        time.sleep(3600)


if __name__ == "__main__":
    main()
