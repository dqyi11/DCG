'''
Created on Dec 1, 2015

@author: walter
'''

from xml.dom.minidom import Document

PHRASE_TYPE = ("S", "VP", "PP", "NP")

def is_phrase_type( type ):
    if type in PHRASE_TYPE:
        return True
    return False

def to_xml(phrase, parentNode, doc):    
    node = doc.createElement(phrase.type)
    parentNode.appendChild(node)
    for w in phrase.words:
        w_node = doc.createElement(w.type)
        w_node.setAttribute("text", w.text)
        node.appendChild(w_node)
    for c in phrase.children:
        to_xml(c, node, doc) 

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
    
    def write_xml(self, filename):
        
        doc = Document()
        
        to_xml(self, doc, doc)
        
        f = open(filename, 'w')
        doc.writexml( f, addindent='  ', newl='\n', encoding='utf-8')
        f.close()
        
   