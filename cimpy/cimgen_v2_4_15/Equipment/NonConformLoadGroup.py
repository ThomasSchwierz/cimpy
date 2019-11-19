from cimpy.cimgen_v2_4_15.Equipment.LoadGroup import LoadGroup


class NonConformLoadGroup(LoadGroup):
	'''
	Loads that do not follow a daily and seasonal load variation pattern.

	:EnergyConsumers: Group of this ConformLoad. Default: []
	:NonConformLoadSchedules: The NonConformLoadSchedules in the NonConformLoadGroup. Default: []
		'''

	

	__doc__ += '\n Documentation of parent class LoadGroup: \n' + LoadGroup.__doc__ 

	def __init__(self, EnergyConsumers = [], NonConformLoadSchedules = [],  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.EnergyConsumers = EnergyConsumers
		self.NonConformLoadSchedules = NonConformLoadSchedules
		
	def __str__(self):
		str = 'class=NonConformLoadGroup\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
