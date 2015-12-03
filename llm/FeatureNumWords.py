'''
Created on Dec 3, 2015

@author: walter
'''

class FeatureNumWords(object):


    def __init__(self):
        self.num_words = 0
        
    def from_xml(self, node, doc):
        self.num_words = int( node.getAttribute("num_words") )
    
    def to_xml(self, parentNode, doc):
        node = doc.createElement("feature_num_words")
        node.setAttribute("num_words", str(self.num_words))
        parentNode.appendChild(node)
        