'''
Created on Dec 1, 2015

@author: walter
'''

from xml.dom import minidom

class World(object):


    def __init__(self):
        self.objects = []

    def from_xml(self):
        pass
    
    def to_xml(self, parentNode, doc):
        world_node = doc.createElement("world")
        parentNode.appendChild(world_node)
        for o in self.objects:
            o.to_xml(world_node, doc)
    
    def write_xml(self, filename):
        doc = minidom.Document()
        self.to_xml(self, doc, doc)
        
        f = open(filename, 'w')
        doc.writexml( f, addindent='  ', newl='\n', encoding='utf-8')
        f.close() 
    
    def read_xml(self, filename):
        pass