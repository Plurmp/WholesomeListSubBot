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
print('Logged in to reddit')

twit = twitter.Api(
    consumer_key=cred['CONSUMER_KEY'],
    consumer_secret=cred['CONSUMER_SECRET'],
    access_token_key=cred['ACCESS_TOKEN'],
    access_token_secret=cred['ACCESS_TOKEN_SECRET']
)
print('Logged in to twitter')

nl = '\n'


def reddit_post(title=None, author=None, tier=None, note=None, pages=None, tags=None, link=None, parody=None,
                uuid=None, feature=False):
    sub = reddit.subreddit("wholesomelist")

    tier_flairs = {
        'S': 'f088234a-b81a-11ea-9e71-0e1dcb1937ef',
        'S-': 'c38f2810-c84c-11ea-84c5-0e35d001c675',
        'A+': 'd802ab6e-c84c-11ea-b3cb-0e3932130613',
        'A': 'fb98aaac-b81a-11ea-a36c-0e34d3f45b33',
        'A-': '416ee70c-c84d-11ea-a6e1-0e6e3dd60dff',
        'B+': '234469be-c84d-11ea-ac70-0e23c18679df',
        'B': '01f3c67a-b81b-11ea-b485-0e35d87bc449',
        'B-': '97f3cd5e-c89d-11ea-8179-0ef049ef4173',
        'C+': '85b5a32e-c89d-11ea-b09c-0e51f7142395',
        'C': '07f2eb96-b81b-11ea-b645-0efb855e960b',
        'C-': '1bc1a0ca-c89e-11ea-bf7e-0e304de417f1',
        'D+': '7f3bda80-cc59-11ea-9e13-0e80adcf2e59',
        'D': '1beb39a0-b81b-11ea-8417-0e9c3b8ed27b',
        'D-': '78a31fc2-cc58-11ea-ac97-0e0856a7f1e3',
    }
    if feature:
        flair = 'dc9b2656-d0f3-11ea-9110-0e298e4654a9'
    else:
        try:
            flair = tier_flairs[tier]
        except KeyError:
            flair = None

    post_id = sub.submit(
        title=f'{"Featured: [" + author + "] " + title if feature else "[" + author + "] " + title}',
        url=link,
        nsfw=True,
        flair_id=flair
    )
    print(f'New item "{title}" posted to r/WholesomeList')

    reddit.submission(id=post_id).reply(
        'Source: \n'
        f'> <{link}>\n\n'
        f'**{title}**  \n'
        f'by {author}\n\n'
        f'Wholesome List link: https://wholesomelist.com/list/{uuid}\n\n'
        f'{"" if (pages == -1 or pages is None) else pages + " pages" + nl + nl}'
        f'Tier: **{tier}**\n\n'
        f'{"" if (note == "None" or note is None) else "**Note:** " + note + nl + nl}'
        f'{"" if (parody is None or parody == "None") else "**Parody: **" + parody + nl + nl}'
        f'{"" if (tags is None) else "**Tags:** " + nl + ", ".join(tags) + nl + nl}'
        '*I am a bot beep boop whatever*'
    )
    print('Replied to reddit post')


def twitter_post(title=None, author=None, tier=None, note=None, pages=None, tags=None, link=None, parody=None,
                 uuid=None, image=None, feature=False):
    post = twit.PostUpdate(
        f'{"Featured:" + nl if feature else "New Entry:" + nl}'
        f'{title}\n'
        f'by {author}\n'
        f'Tier: {tier}\n'
        f'{link}',
        media=image
    )
    twit.PostUpdate(
        f'{"" if (uuid is None) else "Wholesome List link: https://wholesomelist.com/list/" + uuid + nl}'
        f'{"" if (note == "None" or note is None) else "Note: " + note + nl}'
        f'{"" if (parody is None or parody == "None") else "Parody: " + parody + nl}'
        f'{"" if (tags is None) else "Tags: " + ", ".join(tags) + nl}'
        f'{"" if (pages == -1 or pages is None) else pages + " pages"}',
        in_reply_to_status_id=post.id
    )
    print(f'New item "{title}" posted to @WholesomeOf')
