'''
Created on Dec 3, 2015

@author: walter
'''

class FeatureConstraintChildMatchesChildRegion(object):

    def __init__(self):
        self.invert = None
        
    def from_xml(self, node, doc):
        self.invert = int( node.getAttribute("invert") )
    
    def to_xml(self, parentNode, doc):
        node = doc.createElement("feature_constraint_child_matches_child_region")
        node.setAttribute("invert", str(self.invert))
        parentNode.appendChild(node)