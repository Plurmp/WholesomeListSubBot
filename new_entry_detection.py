import submission


def check_new_entry(god_list: list, local_list: list):
    new_entry = False
    for item in god_list:
        if item not in local_list:
            new_entry = True
            print(f'New entry detected: {item}')

            submission.reddit_post(
                title=item['title'],
                author=item['author'],
                tier=item['tier'],
                pages=item['pages'],
                tags=item['tags'],
                link=item['link'],
                warning=item['warning']
            )

            submission.twitter_post(
                title=item['title'],
                author=item['author'],
                tier=item['tier'],
                link=item['link']
            )

            local_list.append(item)
            print(f'Newest local list item is now {local_list[-1]}')
    if not new_entry:
        print('No new entry detected')
