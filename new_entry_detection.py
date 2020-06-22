import json

import submission


def check_new_entry(god_list, local_list):
    for item in god_list:
        if item not in local_list:
            submission.post_doujin(
                title=item["title"],
                author=item["author"],
                tier=item["tier"],
                pages=item["pages"],
                tags=item["tags"],
                link=item["link"]
            )
            with open("local_list.json", "a") as a:
                json.dump(item, a)