import requests
import time

import new_entry_detection

api_list = "https://wholesomelist.com/api/list"
api_features = 'https://wholesomelist.com/api/features'


def remove_id(list1):
    for item in list1:
        del item['id']


def main():
    r_list = requests.get(api_list)
    r_features = requests.get(api_features)
    local_list: list = r_list.json()['table']
    remove_id(local_list)
    local_features: list = r_features.json()['table']
    remove_id(local_features)
    while True:
        r_list = requests.get(api_list)
        r_features = requests.get(api_features)
        god_list: list = r_list.json()['table']
        remove_id(god_list)
        god_features: list = r_features.json()['table']
        remove_id(god_features)
        new_entry_detection.check_new_entry(god_list, local_list, feature=False)
        new_entry_detection.check_new_entry(god_features, local_features, feature=True)
        time.sleep(3600)


if __name__ == "__main__":
    main()
