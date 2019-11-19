from cimpy.cimgen_v2_4_15.Equipment.Equipment import Equipment


class DCConductingEquipment(Equipment):
	'''
	The parts of the DC power system that are designed to carry current or that are conductively connected through DC terminals.

	:DCTerminals:  Default: []
		'''

	

	__doc__ += '\n Documentation of parent class Equipment: \n' + Equipment.__doc__ 

	def __init__(self, DCTerminals = [],  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.DCTerminals = DCTerminals
		
	def __str__(self):
		str = 'class=DCConductingEquipment\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
