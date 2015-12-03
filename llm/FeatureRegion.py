'''
Created on Dec 3, 2015

@author: walter
'''

class FeatureRegion(object):

    def __init__(self):
        self.region_type = None
        
    def from_xml(self, node, doc):
        self.region_type = int( node.getAttribute("region_type") )
    
    def to_xml(self, parentNode, doc):
        node = doc.createElement("feature_region")
        node.setAttribute("region_type", str(self.region_type))
        parentNode.appendChild(node)
        
        