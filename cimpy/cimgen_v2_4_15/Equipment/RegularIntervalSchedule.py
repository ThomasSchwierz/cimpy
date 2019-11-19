from cimpy.cimgen_v2_4_15.Equipment.BasicIntervalSchedule import BasicIntervalSchedule


class RegularIntervalSchedule(BasicIntervalSchedule):
	'''
	The schedule has time points where the time between them is constant.

	:timeStep: The time between each pair of subsequent regular time points in sequence order. Default: 0.0
	:endTime: The time for the last time point. Default: ''
		'''

	

	__doc__ += '\n Documentation of parent class BasicIntervalSchedule: \n' + BasicIntervalSchedule.__doc__ 

	def __init__(self, timeStep = 0.0, endTime = '',  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.timeStep = timeStep
		self.endTime = endTime
		
	def __str__(self):
		str = 'class=RegularIntervalSchedule\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
