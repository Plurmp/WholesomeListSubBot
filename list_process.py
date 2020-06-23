import json


def process(god_list):
    god_list_dict = {}

    with open('local.json', 'w') as w:
        for item in god_list['table']:
            print(type(item))
            god_list_dict[item['link']] = {
                'title': item['title'],
                'author': item['author'],
                'warning': item['warning'],
                'parody': item['parody'],
                'tier': item['tier'],
                'pages': item['pages'],
                'tags': item['tags']
            }
        json.dump(god_list_dict, w)
