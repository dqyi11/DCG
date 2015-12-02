'''
Created on Dec 1, 2015

@author: walter
'''

import os
from nltk.parse import stanford
from nltk.tree import *
from language.Phrase import *
from language.Word import *

os.environ['STANFORD_PARSER'] = '../jars'
os.environ['STANFORD_MODELS'] = '../jars'

class CYKParser(object):

    def __init__(self):
        self.parser = stanford.StanfordParser("../jars/stanford-parser.jar","../jars/stanford-parser-3.4.1-models.jar")
        
    def parse(self, sentence):
        sentences = self.parser.raw_parse_sents( (sentence,) )
        for line in sentences:
            for sentence in line:
                sentence.draw()
                return self.toPhrase( sentence )
            
    def toPhrase(self, tree):
    
        return self.traverseTree( tree )
    
    def traverseTree(self, tree):
        
        if type(tree) is Tree:
            print "LABEL: " + tree.label()
            if tree.label() == "ROOT":
                return self.traverseTree(tree[0])
            #elif tree.label() == "S":
            #    return self.traverseTree(tree[0])
            else:
                p = Phrase()
                p.type = tree.label()
                word_idx = 0
                for subtree in tree:
                    if type(subtree) == Tree:
                        if is_pos_type( subtree.label() ):
                            w = Word()
                            w.type = subtree.label()
                            w.order = word_idx
                            w.text = str( subtree[0] )
                            word_idx += 1
                            p.words.append(w)   
                        elif is_phrase_type( subtree.label() ):
                            child_phrase = self.traverseTree( subtree )
                            p.children.append(child_phrase)
                return p
        return None
        
        