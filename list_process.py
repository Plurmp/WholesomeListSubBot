import json

with open("local_list.json", encoding='utf-8') as file:
    god_list = json.load(file)

with open('local.json', 'w') as w:
    for item in god_list['table']:
        print(type(item))
        json.dump(
            {item['link']: {
                'title': item['title'],
                'author': item['author'],
                'warning': item['warning'],
                'parody': item['parody'],
                'tier': item['tier'],
                'pages': item['pages'],
                'tags': item['tags'],
            }},
            fp=w
        )
