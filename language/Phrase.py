'''
Created on Dec 1, 2015

@author: walter
'''

from xml.dom import minidom
from language.Word import *

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
    
    def write_xml(self, filename):
        doc = minidom.Document()
        root_node = doc.createElement("root")
        doc.appendChild(root_node)
        self.to_xml(root_node, doc)
        
        f = open(filename, 'w')
        doc.writexml( f, addindent='  ', newl='\n', encoding='utf-8')
        f.close()

    def to_xml(self, parentNode, doc):    
        node = doc.createElement(self.type)
        parentNode.appendChild(node)
        for w in self.words:
            w.to_xml(node, doc)
        for c in self.children:
            c.to_xml(node, doc)   
            
    def read_xml(self, filename):
        doc = minidom.parse(filename)
        root_node = doc.getElementsByTagName("root")[0]
        for c in root_node.childNodes:
            if c.nodeType == c.ELEMENT_NODE:
                self.from_xml(c, doc)
    
    def from_xml(self, node, doc):

        self.type = node.nodeName
        for c in node.childNodes:
            if c.nodeType == c.ELEMENT_NODE:

                if is_phrase_type( c.nodeName ):
                    p = Phrase()
                    p.from_xml( c, doc )
                    self.children.append( p )
                
                elif is_pos_type( c.nodeName ):
                    w = Word()
                    w.from_xml( c, doc )   
                    self.words.append( w )        
   