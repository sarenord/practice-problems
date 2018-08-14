import praw
import urllib.request as urllib

reddit = praw.Reddit()
subreddit = reddit.subreddit('wallpapers')
posts = []
for i in subreddit.top('day'):
    posts.append(i.url)
url = posts[0]

urllib.urlretrieve(url, "/home/sarenord/.config/i3/wallpaper.png")
