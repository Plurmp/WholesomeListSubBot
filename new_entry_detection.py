import json

import submission


def check_new_entry(god_list, local_list):
    for item in god_list:
        if item['link'] not in local_list.keys():
            submission.post_doujin(
                title=item["title"],
                author=item["author"],
                tier=item["tier"],
                pages=item["pages"],
                tags=item["tags"],
                link=item["link"]
            )
            with open("local.json", "a") as a:
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
                    fp=a
                )
