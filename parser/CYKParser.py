'''
Created on Dec 1, 2015

@author: walter
'''

import os
from nltk.parse import stanford
from nltk.tree import *
from language.Phrase import *

os.environ['STANFORD_PARSER'] = '../jars'
os.environ['STANFORD_MODELS'] = '../jars'

class CYKParser(object):


    def __init__(self):
        self.parser = stanford.StanfordParser("../jars/stanford-parser.jar","../jars/stanford-parser-3.4.1-models.jar")
        
    def parse(self, sentence):
        sentences = self.parser.raw_parse_sents( (sentence,) )
        for line in sentences:
            for sentence in line:
                return self.toPhrase( sentence )
            
    def toPhrase(self, tree):
    
        if type(tree) is Tree:
            if tree.label() == "ROOT":
                p = self.traverseTree( tree )
                return p
        return None
    
    def traverseTree(self, tree):
        
        p = Phrase()
        for subtree in tree:
            if type(subtree) == Tree:
                self.traverseTree( subtree)
        return p
        
        