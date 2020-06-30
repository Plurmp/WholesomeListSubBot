import praw
from os import environ as cred

reddit = praw.Reddit(
    client_id=cred['CLIENT_ID'],
    client_secret=cred["CLIENT_SECRET"],
    password=cred["PASSWORD"],
    user_agent=cred["USERAGENT"],
    username=cred["USERNAME"]
)


def post_doujin(title, author, tier, warning, pages, tags, link):
    sub = reddit.subreddit("wholesomelist")

    flair = ''
    if tier == 'S':
        flair = 'f088234a-b81a-11ea-9e71-0e1dcb1937ef'
    elif tier == 'A':
        flair = 'fb98aaac-b81a-11ea-a36c-0e34d3f45b33'
    elif tier == 'B':
        flair = '01f3c67a-b81b-11ea-b485-0e35d87bc449'
    elif tier == 'C':
        flair = '07f2eb96-b81b-11ea-b645-0efb855e960b'
    elif tier == 'D':
        flair = '1beb39a0-b81b-11ea-8417-0e9c3b8ed27b'
    else:
        flair = None

    post_id = sub.submit(
        title=f"[{author}] {title}",
        url=link,
        nsfw=True,
        flair_id=flair
    )
    print(f'New item "{title}" posted')

    nl = '\n'

    reddit.submission(id=post_id).reply(
        'Source: \n'
        f'> <{link}>\n\n'
        f'**{title}**  \n'
        f'by {author}\n\n'
        f'{"" if pages == -1 else pages + " pages" + nl + nl}'
        f'Tier: **{tier}**\n\n'
        f'{"" if warning == "None" else "**Warning:**" + warning + nl + nl}'
        f'**Tags:**  \n'
        f'{", ".join(tags)}\n\n'
        '*I am a bot beep boop whatever*'
    )
    print('Reply posted')