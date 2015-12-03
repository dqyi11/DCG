'''
Created on Dec 1, 2015

@author: walter
'''

from parser.CYKParser import *
from language.Phrase import *

if __name__ == '__main__':
    
    SENTENCE1 = "The real voyage of discovery consists not in seeking new landscapes, but in having new eyes."
    SENTENCE2 = "go to the door"
    parser = CYKParser()
    s1 = parser.parse(SENTENCE2)
    
    FILENAME1 = "1.xml"
    FILENAME2 = "2.xml"
    s1.write_xml(FILENAME1)
    
    s2 = Phrase() 
    s2.read_xml(FILENAME1)
    print s2
    s2.write_xml(FILENAME2)