from InstagramAPI import InstagramAPI
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
media_id = info['items'][0]['id']

ig.getMediaLikers(media_id)
f = ig.LastJson['users']
for x in f:
    likes_list.append(x['username'])
    print(x['username'])
    print()
print(len(likes_list))