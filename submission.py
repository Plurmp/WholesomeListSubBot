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
        f"{link}\n\n**{title}**\n\nby {author}\n\n**Tier**: {tier}\n\n{pages} pages\n\n**Tags**\n\n{', '.join(tags)}\n\nWarnings\n\n{', '.join(warning)}\n\n*I am a bot beep boop whatever* "
    )
