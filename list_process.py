import json


def process(god_list):
    god_list_dict = {}

    for item in god_list:
        # print(type(item))
        god_list_dict[item['link']] = {
            'title': item['title'],
            'author': item['author'],
            'warning': item['warning'],
            'parody': item['parody'],
            'tier': item['tier'],
            'pages': item['pages'],
            'tags': item['tags']
        }
