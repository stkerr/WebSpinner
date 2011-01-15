# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="stkerr"
__date__ ="$Jan 14, 2011 8:53:29 PM$"

class Attributes:
    def set_attribute(self, attribute, value):
        # Adds a new attribute
        self.attributes[attribute] = value

    def generate_attribute_string(self):
        output = ""
        for i in range(0,len(self.attributes)):
            output += self.attributes.keys()[i] + "=\"" + self.attributes.values()[i] + "\" "
        return output