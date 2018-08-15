import praw
import urllib.request as urllib
from subprocess import call
import time
import json
import os
import pywal

config = json.load(open("config.json"))
paperpath = config["paperpath"]
cachedir = config["cachedir"]
# date = time.ctime()[9].split(' ')[1:3])
date = time.ctime(os.stat(paperpath)[9]).split(' ')[1:3]

if date != time.ctime(time.time())[1:3]:
	reddit = praw.Reddit()
	subreddit = reddit.subreddit(config["subreddit"])
	for i in subreddit.top('day'):
	    post = i
	    break
	
	urllib.urlretrieve(post.url, paperpath)
	call(["cp", paperpath, cachedir+post.title])

call(["wal", "-i", paperpath, "-g"])

