# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="stkerr"
__date__ ="$Jan 14, 2011 7:59:09 PM$"


class CSS_Properties:

    def add_css_property(self,property,value):
        # Adds a CSS tuple of the form (name, value)
        # to the list of CSS for this node
        self.css_properties.append((property,value))

    def generate_css_property_string(self):
        # Generates the CSS output for this node
        output = ""
        if(len(self.css_properties) > 0):
            output = "style=\""
            for i in self.css_properties:
                output += str(i[0]) + ":" + str(i[1]) + ";"
            output += "\""
        return output