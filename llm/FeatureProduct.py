'''
Created on Dec 1, 2015

@author: walter
'''

from llm.FeatureCV import *
from llm.FeatureWord import *
from llm.FeatureNumWords import *
from llm.FeatureObject import *
from llm.FeatureObjectMatchesChild import *
from llm.FeatureRegion import *
from llm.FeatureRegionMatchesChild import *
from llm.FeatureRegionObject import *
from llm.FeatureRegionObjectMatchesChild import *
from llm.FeatureConstraint import *
from llm.FeatureConstraintParentMatchesChildRegion import *
from llm.FeatureConstraintChildMatchesChildRegion import *
from llm.FeatureConstraintParentIsRobot import *
from llm.FeatureConstraintChildIsRobot import *

class FeatureProduct(object):



    def __init__(self):
        self.feature_groups = []
        
    def to_xml(self, parentNode, doc):    
        node = doc.createElement("feature_product")
        parentNode.appendChild(node)
        for f_g in self.feature_groups:
            group_node = doc.createElement("feature_group")
            node.appendChild(group_node)
            for f in f_g:
                f.to_xml(group_node, doc)
    
    def from_xml(self, node, doc):
        if node.nodeName == "feature_product":
            for c in node.childNodes:
                if c.nodeType == c.ELEMENT_NODE:
                    if c.nodeName == "feature_group":
                        f_g = []
                        self.feature_groups.append(f_g) 
                        for cc in c.childNodes:
                            if cc.nodeType == cc.ELEMENT_NODE:
                                if cc.nodeName == "feature_cv":
                                    f = FeatureCV()
                                    f.from_xml(cc,doc)
                                    f_g.append(f)
                                elif cc.nodeName == "feature_word":
                                    f = FeatureWord()
                                    f.from_xml(cc,doc)
                                    f_g.append(f)
                                elif cc.nodeName == "feature_num_words":
                                    f = FeatureNumWords()
                                    f.from_xml(cc,doc)
                                    f_g.append(f)
                                elif cc.nodeName == "feature_object":
                                    f = FeatureObject()
                                    f.from_xml(cc, doc)
                                    f_g.append(f)
                                elif cc.nodeName == "feature_object_matches_child":
                                    f = FeatureObjectMatchesChild()
                                    f.from_xml(cc, doc)
                                    f_g.append(f)
                                elif cc.nodeName == "feature_region":
                                    f = FeatureRegion()
                                    f.from_xml(cc, doc)
                                    f_g.append(f)
                                elif cc.nodeName == "feature_region_matches_child":
                                    f = FeatureRegionMatchesChild()
                                    f.from_xml(cc, doc)
                                    f_g.append(f)
                                elif cc.nodeName == "feature_region_object":
                                    f = FeatureRegionObject()
                                    f.from_xml(cc, doc)
                                    f_g.append(f)
                                elif cc.nodeName == "feature_region_object_matches_child":
                                    f = FeatureRegionObjectMatchesChild()
                                    f.from_xml(cc, doc)
                                    f_g.append(f)
                                elif cc.nodeName == "feature_constraint":
                                    f = FeatureConstraint()
                                    f.from_xml(cc, doc)
                                    f_g.append(f)
                                elif cc.nodeName == "feature_constraint_parent_matches_child_region":
                                    f = FeatureConstraintParentMatchesChildRegion()
                                    f.from_xml(cc, doc)
                                    f_g.append(f)
                                elif cc.nodeName == "feature_constraint_child_matches_child_region":
                                    f = FeatureConstraintChildMatchesChildRegion()
                                    f.from_xml(cc, doc)
                                    f_g.append(f)
                                elif cc.nodeName == "feature_constraint_parent_is_robot":
                                    f = FeatureConstraintParentIsRobot()
                                    f.from_xml(cc, doc)
                                    f_g.append(f)
                                elif cc.nodeName == "feature_constraint_child_is_robot":
                                    f = FeatureConstraintChildIsRobot()
                                    f.from_xml(cc, doc)
                                    f_g.append(f)
                                    
                                