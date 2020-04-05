from InstagramAPI import InstagramAPI
from collections import Counter
import argparse
import sys

# parse cmd line args
parser = argparse.ArgumentParser(description='Unfollow instagram users that don\'t follow you back!.')
parser.add_argument('username', help='your instagram username')
parser.add_argument('password', help='your instagram password')
parser.add_argument('usernameToTest', help='instagram username to test with')
args = parser.parse_args()

ig = InstagramAPI(args.username, args.password)

# success is just a bool
success = ig.login()
if not success:
    print('INSTAGRAM LOGIN FAILED!')
    sys.exit()

#Gets most recent post from user
ig.searchUsername(args.usernameToTest)
info = ig.LastJson
username_id = info['user']['pk']

likes_list = []

user_posts = ig.getUserFeed(username_id)
info = ig.LastJson

imageCount = len(info['items'])

for i in range(imageCount):
    media_id = info['items'][i]['id']
    likes = ig.getMediaLikers(media_id)
    if not success:
        sys.exit()

    f = ig.LastJson['users']
    for x in f:
        likes_list.append(x['username'])

counted = Counter(likes_list)
print("Top 10 likers out of ", imageCount, " images for user", args.usernameToTest, ":")
for x in counted.most_common(10):
        print(x)