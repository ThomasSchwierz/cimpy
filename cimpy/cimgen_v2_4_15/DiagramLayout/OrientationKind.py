from cimpy.cimgen_v2_4_15.Base import Base


class OrientationKind(Base):
	'''
	The orientation of the coordinate system with respect to top, left, and the coordinate number system.

		'''

	

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=OrientationKind\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
