'''
Created on Dec 1, 2015

@author: walter
'''

from symbol.Object import *
from symbol.Region import *
from symbol.Constraint import *

class GroundingSet(object):

    def __init__(self):
        self.groundings = []
        
    def from_xml(self, node, doc):
        if node.nodeName == "grounding":
            for c in node.childNodes:
                if c.nodeType == c.ELEMENT_NODE:
                    if c.nodeName == "grounding_set":
                        for cc in c.childNodes:
                            if cc.nodeType == cc.ELEMENT_NODE:
                                if c.nodeName == "object":
                                    obj = Object()
                                    obj.from_xml( cc, doc )
                                elif c.nodeName == "region":
                                    reg = Region()
                                    reg.from_xml( cc, doc )
                                elif c.nodeName == "constraint":
                                    cons = Constraint()
                                    cons.from_xml( cc, doc )
                                    
        
    def to_xml(self, parentNode, doc):
        g_node = doc.createElement("grounding")
        parentNode.appendChild(g_node)
        gs_node = doc.createElement("grounding_set")
        g_node.appendChild(gs_node)
        
        for g in self.groundings:
            g.to_xml(gs_node, doc)

        