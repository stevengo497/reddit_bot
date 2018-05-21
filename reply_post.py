import praw
import pdb
import re
import os


reddit = praw.Reddit(client_id='51qL-25HmQG2jw',
                                    client_secret='93CLBwEs99ekSzrqtD7kIhav2ds',
                                    user_agent='Hedberg_Bot',
                                    username='Comedic_Bot',
                                    password='Password123')


if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit('mitchhedberg')
for submission in subreddit.hot(limit=5):
    if submission.id not in posts_replied_to:
        if re.search("mitch hedberg", submission.title, re.IGNORECASE):
            submission.reply("Mitch Hedberg is the G.O.A.T!!!!")
            print("Bot replying to: ", submission.title)
            posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
