'''
Created on Dec 1, 2015

@author: walter
'''

POS_TYPE = ("VB", "TO", "DT", "NN", "JJ", "VBZ", "RB", "IN", "NNS", "VBG", ",", "CC")

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

    def from_xml(self, node, doc):
        self.type = node.nodeName
        self.text = node.getAttribute("text")

    def to_xml(self, parentNode, doc):
        w_node = doc.createElement(self.type)
        w_node.setAttribute("text", self.text)
        parentNode.appendChild(w_node)        