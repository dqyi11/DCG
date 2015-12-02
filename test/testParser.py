'''
Created on Dec 1, 2015

@author: walter
'''

from parser.CYKParser import *

if __name__ == '__main__':
    
    SENTENCE1 = "The real voyage of discovery consists not in seeking new landscapes, but in having new eyes."
    SENTENCE2 = "go to the door"
    parser = CYKParser()
    ss = parser.parse(SENTENCE1)
    
    print ss