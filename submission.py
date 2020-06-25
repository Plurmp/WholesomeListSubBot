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

    post_id = sub.submit(
        title=f"[{author}] {title}",
        url=link,
        nsfw=True
    )

    reddit.submission(id=post_id).reply(
        'Source:\n'
        f'> <{link}>\n\n'
        f'**{title}**  \n'
        f'by {author}\n\n'
        f'{"" if pages == -1 else pages + " pages\n\n"}'
        f'Tier: **{tier}**\n\n'
        f'{"" if warning == "None" else "**Warning:**" + warning + "\n\n"}'
        f'**Tags:**  \n'
        f'{", ".join(tags)}\n\n'
        '*I am a bot beep boop whatever*'
    )
