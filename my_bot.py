import praw

reddit = praw.Reddit(client_id='51qL-25HmQG2jw',
                                    client_secret='93CLBwEs99ekSzrqtD7kIhav2ds',
                                    user_agent='Hedberg_Bot',
                                    username='Comedic_Bot',
                                    password='Password123')

reddit.read_only = True
subreddit = reddit.subreddit('mitchhedberg')
hot_mitch = subreddit.hot(limit=5)

for submission in hot_mitch:
    print(submission.title)
    print(submission.id)
