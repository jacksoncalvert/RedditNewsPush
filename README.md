# redditNews
Overnight tool using the Reddit API to send yourself the top new articles from overnight/the last day. 

# How to Run
This script is desinged to be used on a Virtual env and run every day using cron or another scheduling tool. 

For use with emails, download the redditpush and emailscript files. You will need to enable unauthroised access opn your gamil account, so creating a dummy account is recommended. 

You will need to activate the Reddit API for your account. A guide can be seen here -> https://github.com/reddit-archive/reddit/wiki/OAuth2

Edit the "redditpush" file to your preffered subreddit. "emailScript" will take this list and send it to your desired email address.

My loaded my script to an EC2 instance on AWS and ran it every day at 5am with cron. 
