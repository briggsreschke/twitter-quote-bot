# Grab a random quote from line in text file

import csv
import random

def thought():
    quotes = []
    
    with open('42.txt', 'r') as f:
        try:
            quotes = f.readlines()
        except:
            print('DON\'T PANIC!')

    nquotes = len(quotes)
    return quotes[random.randint(0, nquotes - 1)]
