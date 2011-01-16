class Validator:
	
	def __init__(self):
		pass

	def validate(self):
		"""
		 Validates the given node against what 
		is required by this node
		"""

		# Copy the required attributes temporarily
		temp_attributes = self.required_attributes[:]

		for i in self.attributes:
			if i in temp_attributes:
				temp_attributes.remove(i)

		if len(temp_attributes) > 0:
			print "Node " + self.tag_string + " is missing required attributes!"
			return False
		
		for i in self.children:
			if i.validate() is False:
				return False

		return True