'''
Created on Dec 1, 2015

@author: walter
'''

class FeatureCV(object):

    def __init__(self):
        self.cv = None
        
    def from_xml(self, node, doc):
        self.cv = int( node.getAttribute("cv") )
    
    def to_xml(self, parentNode, doc):
        node = doc.createElement("feature_cv")
        node.setAttribute("cv", str(self.cv))
        parentNode.appendChild(node)