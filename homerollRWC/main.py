import praw
import urllib.request as urllib
from subprocess import call
paperpath = "/home/sarenord/.config/i3/wallpaper.png"
cachedir = "/home/sarenord/Pictures/wallpapers/"
reddit = praw.Reddit()
subreddit = reddit.subreddit('wallpapers')
for i in subreddit.top('day'):
    post = i
    break

urllib.urlretrieve(post.url, paperpath)
call(["cp", paperpath, cachedir+post.title])
