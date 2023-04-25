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

TWITTER_HANDLE = "HHGuideBot"
LAST_N_TWEETS =40 
QUOTES = "Projects/Twitter/bots/hhg/42.txt"
TESTING = True


# Create tweepy api
def create_api():

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return tweepy.API(auth)


# Get last_number_of_tweets timeline
def get_timeline_history(client, LAST_N_TWEETS, twitter_name):

    tweets = client.user_timeline(
        screen_name=twitter_name, count=LAST_N_TWEETS, tweet_mode="extended")
     
    return [tweet.full_text.rstrip() for tweet in tweets]


# Read quotes in from a .txt file and format
def get_quotes(fname, parser):
    
    with open(fname, 'r') as file:
        return [parser(line).rstrip() for line in file]

    
# Return a random quote to tweet from list of quotes
def get_random(quotes):
    return quotes[random.randint(0, len(quotes) - 1)]


# Get path for system testing/running on
def path():
    
    if platform.system() == 'Linux':
        return "/home/briggs/" + QUOTES
    else:
        return "/Users/briggs/" + QUOTES
        

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
    # create tweepy api
    client = create_api()

    # read full quotes database
    quotes = get_quotes(path(), parser)
    
    # get last n tweets from timeline
    history = get_timeline_history(client, LAST_N_TWEETS, TWITTER_HANDLE)
    
    # get quotes that are not in last_n_tweets
    diff = list(set(quotes) - set(history))

    # random quote and tweet
    tweet = get_random(diff)
    
    if TESTING == True:
        print(tweet)
    else:
        client.update_status(tweet)


if __name__ == "__main__":
    main()