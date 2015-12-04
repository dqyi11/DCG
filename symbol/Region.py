'''
Created on Dec 3, 2015

@author: walter
'''

from symbol.Object import *

class Region(object):


    def __init__(self):
        self.type = None
        self.object = None
        
    def from_xml(self, node, doc):
        self.type = node.getAttribute("type")
        for c in node.childNodes:
            if c.nodeType == c.ELEMENT_NODE:
                if c.nodeName == "object":
                    self.object = Object()
                    self.object.from_xml( c, doc )
    
    def to_xml(self, parentNode, doc):
        node = doc.createElement("region")
        parentNode.appendChild(node)
        node.setAttribute("type", self.type)
        if self.object != None:
            self.object.to_xml(node, doc)
        