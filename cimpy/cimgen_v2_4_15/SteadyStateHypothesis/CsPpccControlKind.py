from cimpy.cimgen_v2_4_15.Base import Base


class CsPpccControlKind(Base):
	'''
	Active power control modes for HVDC line operating as Current Source Converter.

		'''

	

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=CsPpccControlKind\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
