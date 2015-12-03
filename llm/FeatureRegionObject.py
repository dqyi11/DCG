'''
Created on Dec 3, 2015

@author: walter
'''

class FeatureRegionObject(object):

    def __init__(self):
        self.object_type = None
        
    def from_xml(self, node, doc):
        self.object_type = int( node.getAttribute("object_type") )
    
    def to_xml(self, parentNode, doc):
        node = doc.createElement("feature_region_object")
        node.setAttribute("object_type", str(self.object_type))
        parentNode.appendChild(node)