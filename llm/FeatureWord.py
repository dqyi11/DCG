'''
Created on Dec 3, 2015

@author: walter
'''

class FeatureWord(object):

    def __init__(self):
        self.text = None
        self.pos = None
        
    def from_xml(self, node, doc):
        self.text = node.getAttribute("text")
        self.pos = node.getAttribute("pos")
    
    def to_xml(self, parentNode, doc):
        node = doc.createElement("feature_word")
        node.setAttribute("text", str(self.text))
        node.setAttribute("pos", str(self.pos))
        parentNode.appendChild(node)
        