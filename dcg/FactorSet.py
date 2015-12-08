'''
Created on Dec 1, 2015

@author: walter
'''

class FactorSetSolution(object):
    
    def __init__(self):
        self.cv = []
        self.children = []
        self.groudnings = []
        self.pygx = 0.0

class FactorSet(object):

    def __init__(self, phrase):
        self.phrase = phrase
        self.children = []
        self.solutions = []
        
    
        