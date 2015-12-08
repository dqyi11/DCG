'''
Created on Dec 1, 2015

@author: walter
'''

import sys, getopt
from llm.FeatureSet import *
from llm.LLM import *

def evaluate_model( llm, examples ):
    pass

def evaluate_cv( grounding, grounding_set ):
    pass

def scrape_examples( phrase, world, search_spaces, examples ):
    pass

if __name__ == '__main__':
    
    FEATURE_SET_FILENAME = ''
    OUTPUT_FILENAME = ''
    
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hf:o",["feature_set=","output="])
    except getopt.GetoptError:
        print 'LLMTrain.py -f <feature_set.xml> -o <output.xml>'
        sys.exit(2)
    for opt,arg in opts, args:
        if opt == '-h':
            print 'LLMTrain.py -f <feature_set.xml> -o <output.xml>'
        elif opt in ("-f", "--feature_set"):
            FEATURE_SET_FILENAME = arg
        elif opt in ("-o", "--output"):
            OUTPUT_FILENAME = arg
    
    feature_set = FeatureSet()
    feature_set.read_xml( FEATURE_SET_FILENAME )
    
    llm = LLM( feature_set )
    