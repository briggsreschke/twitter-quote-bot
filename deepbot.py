import random
import tweepy
import platform
import os

from auth import (
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET
)

LAST_N_TWEETS =40 
FILE = "/Projects/Twitter/bots/hhg/42.txt"
TESTING = True


def create_api():

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return tweepy.API(auth)


# Get LAST_N_TWEETS from timeline so that quotes aren't posted more than once in succession

def get_timeline_history(client, LAST_N_TWEETS, twitter_name):

    tweets = client.user_timeline(
        screen_name=twitter_name, count=LAST_N_TWEETS, tweet_mode="extended")
    return [tweet.full_text.rstrip() for tweet in tweets]


# Read quotes in from a .txt file and prettyfy

def get_quotes(fname, parser):

    quotes = []

    with open(fname, 'r') as file:
        quotes = [parser(line).rstrip() for line in file]
    return quotes

# Return a random quote to tweet from list of quotes


def get_random(quotes):

    random.shuffle(quotes)
    quote = quotes[random.randint(0, len(quotes) - 1)]
    return(quote)


# Get path for system testing/running on
def path():

    if platform.system() == 'Linux':
        path = "/home/briggs" + FILE
    else:
        path = "/Users/briggs" + FILE
    return path

# Parse quotes so they match timeline newlines, etc..


def parser(line):

    if line.find('\\n'):  # Enforce newline for quotes with paragraphs
        line = line.replace('\\n', '\n')
    if line.find('/'):  # Poetry line seperator
        line = line.replace('/', '\n')

    # strip trailing \n and return
    return(line.rstrip('\n'))

# Main loop


def main():
    # create API
    client = create_api()

    # get last n tweets from timeline
    history = get_timeline_history(client, LAST_N_TWEETS, 'HHGuideBot')
    # read quotes database
    quotes = get_quotes(path(), parser)
    # get quotes that are not in timeline history (last n tweets)
    diff = list(set(quotes)-set(history))

    # random quote and tweet
    tweet = diff[random.randint(0, len(diff) - 1)]
    if TESTING == True:
        print(tweet)
    else:
        client.update_status(tweet)


if __name__ == "__main__":
    main()
