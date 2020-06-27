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
                link=item["link"],
                warning=item['warning']
            )

            local_list.append(item)
