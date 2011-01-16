# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="stkerr"
__date__ ="$Jan 14, 2011 8:14:04 PM$"

import sys

class Render_Engine():

    def render_tabified(self):
        # Render's the document with each level of children at a higher
        # indentation level than the last
        output = ""
        output += self.render_tabified_loop(0)
        return output

    def render(self):
        # Render this node as well as it's children
        output = ""
        output += self.render_open(0) + "\n"

        for i in self.children:
            output += i.render() + "\n"
        
        output += self.render_close(0) + "\n"
        return output
    def render_tabified_loop(self, depth):
        # Internal helper function
        output = ""
        for i in range(0, depth):
            output += "\t"
        output += self.render_open() + "\n"

        if self.render_middle() != "":
            for i in range(0, depth+1):
                output += "\t"
            output += self.render_middle() + "\n"
        
        for i in self.children:
            output += i.render_tabified_loop(depth+1)
        
        for i in range(0, depth):
            output += "\t"
        output += self.render_close() + "\n"

        return output

    def render_open(self):
        output = ""
        output += "<" + self.tag_string + " "
        css_string = self.generate_css_property_string()
        if(css_string != ""):
            output += css_string
        js_string = self.generate_javascript_property_string()
        if(js_string != ""):
            output += js_string

        attribute_string = self.generate_attribute_string()
        if(attribute_string != ""):
            output += attribute_string
        output += ">"

        return output

    def render_middle(self):
        output = ""
        output += self.text
        return output

    def render_close(self):
        output = ""
        output += "</" + self.tag_string + ">"
        return output
