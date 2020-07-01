import submission


def check_new_entry(god: list, local: list, feature: bool):
    new_entry = False
    for item in god:
        if item not in local:
            new_entry = True
            if feature:
                print(f'New feature detected: {item}')
            else:
                print(f'New entry detected: {item}')

            submission.reddit_post(
                title=item['title'],
                author=item['author'],
                tier=item['tier'],
                pages=item['pages'],
                tags=item['tags'],
                link=item['link'],
                warning=item['warning'],
                feature=feature
            )

            submission.twitter_post(
                title=item['title'],
                author=item['author'],
                tier=item['tier'],
                link=item['link'],
                feature=feature
            )

            local.append(item)
            if feature:
                print(f'Newest local feature item is now {local[-1]}')
            else:
                print(f'Newest local list item is now {local[-1]}')
    if not new_entry:
        if feature:
            print('No new feature detected')
        else:
            print('No new entry detected')
