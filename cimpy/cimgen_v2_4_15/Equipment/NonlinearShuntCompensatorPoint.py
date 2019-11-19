from cimpy.cimgen_v2_4_15.Base import Base


class NonlinearShuntCompensatorPoint(Base):
	'''
	A non linear shunt compensator bank or section admittance value.

	:NonlinearShuntCompensator: Non-linear shunt compensator owning this point. Default: None
	:b: Positive sequence shunt (charging) susceptance per section Default: 0.0
	:g: Positive sequence shunt (charging) conductance per section Default: 0.0
	:sectionNumber: The number of the section. Default: 0.0
	:b0: Zero sequence shunt (charging) susceptance per section Default: 0.0
	:g0: Zero sequence shunt (charging) conductance per section Default: 0.0
		'''

	

	

	def __init__(self, NonlinearShuntCompensator = None, b = 0.0, g = 0.0, sectionNumber = 0.0, b0 = 0.0, g0 = 0.0,  ):
	
		self.NonlinearShuntCompensator = NonlinearShuntCompensator
		self.b = b
		self.g = g
		self.sectionNumber = sectionNumber
		self.b0 = b0
		self.g0 = g0
		
	def __str__(self):
		str = 'class=NonlinearShuntCompensatorPoint\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
