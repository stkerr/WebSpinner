"""
The node class that all other elements will derive from
Note that this class is abstract, and should never be derived directly
"""

__author__ = "stkerr"
__date__ = "$Jan 14, 2011 10:30:42 AM$"

import sys
from attributes import *
from css_properties import *
from javascript_properties import *
from render_engine import *
from validator import *

class Node(CSS_Properties, Javascript_Properties, Attributes, Render_Engine, Validator):

    def __init__(self, parent=None, nodeid=None, nodeclass=None, text=None):
        self.myinit()
        if(parent != None):
            self.set_parent(parent)
        if(nodeid != None):
            self.set_attribute("id", nodeid)
        if(nodeclass != None):
            self.set_attribute("class", nodeclass)
        if(text != None):
            self.set_text(text)

    def myinit(self):
        # Any child nodes
        self.children = []

        # Any CSS styling
        self.css_properties = []

        # Any javascript
        self.js_properties = []

        # Any text contained in the tags
        self.text = ""

        # Tag attributes
        self.attributes = {}


    def add_child(self, child_node):
        self.children.append(child_node)

    def set_parent(self, newparent):
        if(type(self) != type(newparent)):
            print("Invalid set_parent call!")
        newparent.children.append(self)

    def set_text(self, newtext):
        self.text = newtext