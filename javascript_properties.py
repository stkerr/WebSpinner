# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="stkerr"
__date__ ="$Jan 14, 2011 8:28:00 PM$"

class Javascript_Properties:

    def add_javascript_property(self,property,value):
        # Adds a Javascript tuple of the form (name, value)
        # to the list of CSS for this node
        self.js_properties.append((property,value))

    def generate_javascript_property_string(self):
        # Generates the CSS output for this node
        output = ""
        if(len(self.js_properties) > 0):
            for i in self.js_properties:
                output += str(i[0]) + "=\"" + str(i[1]) + ";\""
        return output