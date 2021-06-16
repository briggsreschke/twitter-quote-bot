from deepthought import *

# Main ----
LAST_N_TWEETS = 10
FILE = "42.txt"

def main():  
    client = create_api()             

    timeline_history = get_timeline_history(client, LAST_N_TWEETS)  
    quotes = get_quotes(FILE)
    
    tweet = get_random(quotes)
    while(tweet in timeline_history):
        tweet = get_random(quotes)

    client.update_status(tweet)
    #print(tweet)

if __name__ == "__main__":
    main()
