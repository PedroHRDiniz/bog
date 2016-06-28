from nltk.twitter import Query, Twitter, credsfromfile

usernames = ['pedro_diniz_', 'pedrootorres']
oauth = credsfromfile()
client = Query(**oauth)
def get_user_info(usernames):
    return [client.show_user(screen_name=username) for username in usernames]

user_info = get_user_info(usernames)

for info in user_info:
    name = info['screen_name']
    followers = info['followers_count']
    following = info['friends_count']
    print("{}, followers: {}, following: {}".format(name, followers, following))