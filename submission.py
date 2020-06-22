import praw

reddit = praw.Reddit(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    password="PASSWORD",
    user_agent="USERAGENT",
    username="USERNAME"
)


def post_doujin(title, author, tier, warnings, pages, tags, link):
    sub = reddit.subreddit("wholesomelist")

    post_id = sub.submit(
        title=f"[{author}] {title}",
        url=link,
        nsfw=True
    )

    reddit.submission(id=post_id).reply(
        f"{link}\n\n**{title}**\n\nby {author}\n\n**Tier**: {tier}\n\n{pages} pages\n\n**Tags**\n\n{', '.join(tags)}\n\nWarnings\n\n{', '.join(warnings)}\n\n*I am a bot beep boop whatever* "
    )
