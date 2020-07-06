import praw
import twitter
from os import environ as cred

reddit = praw.Reddit(
    client_id=cred['CLIENT_ID'],
    client_secret=cred["CLIENT_SECRET"],
    password=cred["PASSWORD"],
    user_agent=cred["USERAGENT"],
    username=cred["USERNAME"]
)

twit = twitter.Api(
    consumer_key=cred['CONSUMER_KEY'],
    consumer_secret=cred['CONSUMER_SECRET'],
    access_token_key=cred['ACCESS_TOKEN'],
    access_token_secret=cred['ACCESS_TOKEN_SECRET']
)


def reddit_post(title, author, tier, warning, pages, tags, link, feature: bool):
    sub = reddit.subreddit("wholesomelist")

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
        title=f'{"Featured: [" + author + "] " + title if feature else "[" + author + "] " + title}',
        url=link,
        nsfw=True,
        flair_id=flair
    )
    print(f'New item "{title}" posted to r/WholesomeList')

    nl = '\n'

    reddit.submission(id=post_id).reply(
        'Source: \n'
        f'> <{link}>\n\n'
        f'**{title}**  \n'
        f'by {author}\n\n'
        f'{"" if (pages == -1 or pages is None) else pages + " pages" + nl + nl}'
        f'Tier: **{tier}**\n\n'
        f'{"" if (warning == "None" or warning is None) else "**Warning:**" + warning + nl + nl}'
        f'{"" if (tags is None) else "**Tags:** " + nl + ", ".join(tags) + nl + nl}'
        '*I am a bot beep boop whatever*'
    )
    print('Replied to reddit post')


def twitter_post(title, author, tier, link, feature: bool):
    nl = '\n'
    twit.PostUpdate(
        f'{"Featured:" + nl if feature else "New Entry:" + nl}'
        f'{title}\n'
        f'by {author}\n'
        f'Tier: {tier}\n'
        f'{link}'
    )
    print(f'New item "{title}" posted to @WholesomeOf')
