import requests
import json
import time

import new_entry_detection

api = "https://wholesomelist.com/api/list"


def main():
    r = requests.get(api)
    god_list = r.json()["table"]
    with open('local.json') as file:
        local_list = json.load(file)
    while True:
        new_entry_detection.check_new_entry(god_list, local_list)
        time.sleep(3600)


if __name__ == "__main__":
    main()
