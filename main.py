import praw
import random
#needs a praw.ini file to work properly
my_reddit = praw.Reddit('mirkwoodbot')
my_subreddit = my_reddit.subreddit('MirkwoodGang')


dan_roasts = ["The 2011 Saab 9-3 is based off of the Chevy Malibu", "There is only one person in Mirkwood that has Wu-Tanged a Juul pod", "Dan is known for his affinity for sloppy seconds"]

#adapted from https://github.com/acini/praw-antiabuse-functions/blob/master/anti-abuse.py
def is_done(post_id):
    """
    Checks to see if this post has already been replied to
    :param post_id:
    :return:
    """
    global my_reddit
    post = my_reddit.comment(post_id).refresh()
    done = False
    reply_num = 0
    try:
        reply_num = len(post.replies.list())
    except:
        pass
    if reply_num > 0:
        for reply in post.replies:
            if reply.author is not None and reply.author.name == "mirkwoodbot":
                done = True
                break


    return done

reply_num = 0

for entry in my_subreddit.top():
    for com in entry.comments:
        if '!roastdan' in com.body:
            if not is_done(com.id):
                com.reply(dan_roasts[random.randint(0, len(dan_roasts)-1)] + ' ^I ^am ^a ^bot...')
                reply_num += 1
        for repl in com.replies.list():
            if '!roastdan' in repl.body:
                if not is_done(repl.id):
                    repl.reply(dan_roasts[random.randint(0, len(dan_roasts) - 1)] + ' ^I ^am ^a ^bot...')
                    reply_num += 1



print('number of roasts this session:', reply_num)
