# Take quote (thought) and print it to the terminal
# chop each line off at white space so words aren't broken

from deep_thought import thought
import os

ts = os.get_terminal_size()
cols = ts.columns
thought = thought()

while(thought):
    line = thought[:cols-1]
    if(len(line) >= cols-1):
        line = line.rsplit(' ', 1)[0]
    print(line) 
    
    thought = thought[len(line)+1:]
    

    
    

