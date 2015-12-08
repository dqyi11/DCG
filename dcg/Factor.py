'''
Created on Dec 1, 2015

@author: walter
'''

from symbol.CV import *

class Factor(object):


    def __init__(self, cv, grounding, phrase, world, children, llm, cvs, solution_idx):
        self.cv = cv
        self.grounding = grounding
        self.phrase = phrase
        self.world = world
        self.children = children
        self.llm = llm
        self.cvs = cvs
        self.solution_idx = solution_idx
        self.pygx = 0.0
        
    def value(self, cv ):
        if self.llm != None:
            children = []
            for c in self.children:
                if len(self.children.cvs) == 2:
                    if c.cv == CV_TRUE:
                        children.append( c.grounding )
                elif len(self.children.cvs) == 3:
                    if c.cv == CV_INVERTED or c.cv == CV_TRUE:
                        children.append( c.grounding )                
            self.pygx = self.llm.pygx( self.cv, self.grounding, children, self.phrase, self.world, self.cvs )
            return self.pygx
        return 0.5
    
    