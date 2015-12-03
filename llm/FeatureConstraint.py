'''
Created on Dec 1, 2015

@author: walter
'''

class FeatureConstraint(object):

    def __init__(self):
        self.constraint_type = None
        
    def from_xml(self, node, doc):
        self.region_type = int( node.getAttribute("constraint_type") )
    
    def to_xml(self, parentNode, doc):
        node = doc.createElement("feature_constraint")
        node.setAttribute("constraint_type", str(self.constraint_type))
        parentNode.appendChild(node)