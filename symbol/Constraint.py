'''
Created on Dec 1, 2015

@author: walter
'''

from symbol.Region import *

class Constraint(object):

    def __init__(self):
        self.type = None
        self.parent = None
        self.child = None
        
    def from_xml(self, node, doc):
        self.type = node.getAttribute("type")
        for c in node.childNodes:
            if c.nodeType == c.ELEMENT_NODE:
                if c.nodeName == "parent":
                    for cc in c.childNodes:
                        if cc.nodeType == cc.ELEMENT_NODE:
                            if cc.nodeName == "region":
                                self.parent = Region()
                                self.parent.from_xml( cc, doc )
                elif c.nodeName == "child":
                    for cc in c.childNodes:
                        if cc.nodeType == cc.ELEMENT_NODE:
                            if cc.nodeName == "region":
                                self.child = Region()
                                self.child.from_xml( cc, doc )                    
    
    def to_xml(self, parentNode, doc):
        node = doc.createElement("region")
        parentNode.appendChild(node)
        node.setAttribute("type", self.type)
        if self.parent != None:
            p_node = doc.createElement("parent")
            node.appendChild(p_node)
            self.parent.to_xml(p_node, doc)
        if self.child != None:
            c_node = doc.createElement("child")
            node.appendChild(c_node)
            self.child.to_xml(c_node, doc)
            
            