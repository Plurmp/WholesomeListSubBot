import submission


def check_new_entry(god_list: list, local_list: list):
    for item in god_list:
        if item not in local_list:
            new_entry = True
            print(f'New entry detected: {item}')

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
            print(f'Newest local list item is now {local_list[-1]}')
    if not new_entry:
        print('No new entry detected')
