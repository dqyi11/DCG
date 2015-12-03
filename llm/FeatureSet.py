'''
Created on Dec 1, 2015

@author: walter
'''

from xml.dom import minidom
from llm.FeatureProduct import FeatureProduct

class FeatureSet(object):


    def __init__(self):
        self.feature_products = []
 
    def write_xml(self, filename):
        doc = minidom.Document()
        root_node = doc.createElement("root")
        doc.appendChild(root_node)
        self.to_xml(root_node, doc)
        
        f = open(filename, 'w')
        doc.writexml( f, addindent='  ', newl='\n', encoding='utf-8')
        f.close()

    def to_xml(self, parentNode, doc):    
        node = doc.createElement("feature_set")
        parentNode.appendChild(node)
        for f_p in self.feature_products:
            f_p.to_xml(node, doc)
            
    def read_xml(self, filename):
        doc = minidom.parse(filename)
        root_node = doc.getElementsByTagName("root")[0]
        for c in root_node.childNodes:
            if c.nodeType == c.ELEMENT_NODE:
                self.from_xml(c, doc)
    
    def from_xml(self, node, doc):
        if node.nodeName == "feature_set":
            for c in node.childNodes:
                if c.nodeType == c.ELEMENT_NODE:
                    f_p = FeatureProduct()
                    f_p.from_xml(c, doc)
                    self.feature_products.append( f_p )
