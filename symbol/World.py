'''
Created on Dec 1, 2015

@author: walter
'''

from xml.dom import minidom
from symbol.Object import *

class World(object):


    def __init__(self):
        self.objects = []
    
    def write_xml(self, filename):
        doc = minidom.Document()
        self.to_xml(self, doc, doc)
        
        f = open(filename, 'w')
        doc.writexml( f, addindent='  ', newl='\n', encoding='utf-8')
        f.close() 
        
    def to_xml(self, parentNode, doc):
        world_node = doc.createElement("world")
        parentNode.appendChild(world_node)
        for o in self.objects:
            o.to_xml(world_node, doc)    
            
    def read_xml(self, filename):
        doc = minidom.parse(filename)
        root_node = doc.getElementsByTagName("root")[0]
        for c in root_node.childNodes:
            if c.nodeType == c.ELEMENT_NODE:
                self.from_xml(c, doc)
                
    def from_xml(self, node, doc):
        for c in node.childNodes:
            if c.nodeType == c.ELEMENT_NODE:
                if c.nodeName == "object":
                    o = Object()
                    o.from_xml( c, doc )
                    self.objects.append( o )
                    
