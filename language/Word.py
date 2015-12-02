'''
Created on Dec 1, 2015

@author: walter
'''

POS_TYPE = ["VB", "TO", "DT", "NN"]

def is_pos_type( type ):
    if type in POS_TYPE:
        return True
    return False

class Word(object):


    def __init__(self):
        self.type = None
        self.text = ""
        self.order = -1
        
    def __repr__(self):
        return str(self.type) + ":" + self.text

        