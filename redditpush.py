import praw
# This is a script with function newsList() that grabs the latest news articles from
# Reddit to send either through a text message or email, depending on what you want.
# this script will return a list with titles and links to the top 5 articles from r/WorldNews
# from the past 24 hours.

def newsList():
    reddit = praw.Reddit(client_id='your client id here',
                         client_secret='your client_secret here', password='#####',
                         user_agent='PrawTut', username='#####')

    subreddit = reddit.subreddit('python')

    hot_python = subreddit.hot(limit=1)

    news = reddit.subreddit("worldnews")

    news_top = news.top("day", limit=5)

    list = []
    for submission in news_top:
        list.append(submission.title[0:100] + "... : " + submission.url)

    return list
