'''
Created on Dec 1, 2015

@author: walter
'''

from xml.dom import minidom

class Object(object):



    def __init__(self):
        self.name = ""
        self.type = ""
        
    def to_xml(self, parentNode, doc):    
        node = doc.createElement("object")
        parentNode.appendChild(node)
        node.setAttribute("name", self.name)
        node.setAttribute("type", self.type)
        
    def from_xml(self, node, doc):        
        self.name = node.getAttribute("name")
        self.type = node.getAttribute("type")
            
        