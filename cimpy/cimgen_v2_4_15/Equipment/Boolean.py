from cimpy.cimgen_v2_4_15.Base import Base


class Boolean(Base):
	'''
	A type with the value space "true" and "false".

		'''

	

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=Boolean\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
