from InstagramAPI import InstagramAPI
from collections import Counter
import argparse

likes_list = []

# parse cmd line args
parser = argparse.ArgumentParser(description='Unfollow instagram users that don\'t follow you back!.')
parser.add_argument('username', help='your instagram username')
parser.add_argument('password', help='your instagram password')
args = parser.parse_args()

ig = InstagramAPI(args.username, args.password)

# success is just a bool
success = ig.login()
if not success:
    print('INSTAGRAM LOGIN FAILED!')
    sys.exit()

ig.searchUsername(args.username) #Gets most recent post from user
info = ig.LastJson
username_id = info['user']['pk']
user_posts = ig.getUserFeed(username_id)
info = ig.LastJson

for i in range(15):
    media_id = info['items'][i]['id']
    ig.getMediaLikers(media_id)
    f = ig.LastJson['users']
    for x in f:
        likes_list.append(x['username'])

counted = Counter(likes_list)
print(counted.most_common(5))