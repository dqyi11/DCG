'''
Created on Dec 1, 2015

@author: walter
'''

PHRASE_TYPE = ("S", "VP", "PP", "NP")

def is_phrase_type( type ):
    if type in PHRASE_TYPE:
        return True
    return False

class Phrase(object):


    def __init__(self):
        self.type = None
        self.text = ""
        self.words = []
        self.children = []
        
    def __repr__(self):
        str_repr = "(" + str(self.type) + " ["
        for w in self.words:
            str_repr += w.__repr__() + " "
        str_repr += "] "
        for c in self.children:
            str_repr += c.__repr__()
        str_repr += ")"
        return str_repr
        