# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="stkerr"
__date__ ="$Jan 14, 2011 8:14:04 PM$"

import sys
class Render_Engine:

    def render_tabified(self):
        # Render's the document with each level of children at a higher
        # indentation level than the last
        self.render_open(0)
        for i in self.children:
            i.render_tabified_loop(1)
        self.render_close(0)

    def render_tabified_loop(self, depth):
        # Internal helper function
        self.render_open(depth)
        for i in self.children:
         #   for j in range(0, depth):
        #        sys.stdout.write("\t")
            i.render_tabified_loop(depth+1)

        self.render_close(depth)

    def render(self):
        # Render this node as well as it's children
        self.render_open(0)
        for i in self.children:
            i.render()
        self.render_close(0)

    def render_open(self, depth):
       # print "Open depth: " + str(depth)
        for i in range(0, depth):
            sys.stdout.write("\t")

        print "<" + self.tag_string,
        css_string = self.generate_css_property_string()
        if(css_string != ""):
            print css_string,
        js_string = self.generate_javascript_property_string()
        if(js_string != ""):
            print js_string,

        attribute_string = self.generate_attribute_string()
        if(attribute_string != ""):
            print attribute_string,
        print ">"

        if(self.text != ""):
            for i in range(0, depth+1):
                sys.stdout.write("\t")
            print self.text


    def render_close(self, depth):
        #print "Close depth: " + str(depth)
        for i in range(0, depth):
                sys.stdout.write("\t")
        print "</" + self.tag_string + ">"
