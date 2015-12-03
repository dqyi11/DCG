'''
Created on Dec 3, 2015

@author: walter
'''

from llm.FeatureSet import *

if __name__ == '__main__':
    
    FILENAME1 = "feature_set.xml"
    FILENAME2 = "feature_set1.xml"
    
    feature_set = FeatureSet()
    feature_set.read_xml(FILENAME1)
    feature_set.write_xml(FILENAME2)