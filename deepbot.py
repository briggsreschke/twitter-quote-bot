from deepthought import *
import platform, os

LAST_N_TWEETS = 20 
FILE = "/Twitter/deepthought/bot/42.txt"
_TESTING_ = False 

def get_path():
    if platform.system() == 'Linux':
        path = "/home/briggs" + FILE
    else:
        path = "/Users/briggs" + FILE

    return path

# Parse quotes so they match timeline and tweet pretty

def parser(line):

    if line.find('\\n'): # Enforce newline for quotes with paragraphs
        line = line.replace('\\n', '\n')
    if line.find('/'):  #Poetry line seperator
        line = line.replace('/', '\n')

    #strip trailing \n and return
    return(line.rstrip())


# Main loop           

def main():  

    client = create_api()             

    
    timeline_history = get_timeline_history(client, LAST_N_TWEETS)  
    quotes = get_quotes(get_path(), parser)

    if _TESTING_ == True:
        while(True):
            os.system('clear')
            tweet = get_random(quotes)
            while(tweet in timeline_history):
                print("FLAGED:\n" + tweet + '\n')
                tweet = get_random(quotes)
            print(tweet)
            input('')
    else:  
        tweet = get_random(quotes)
        while(tweet in timeline_history):
            tweet = get_random(quotes)

        client.update_status(tweet)

        
if __name__ == "__main__":
    main()
