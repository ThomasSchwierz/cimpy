from cimpy.cimgen_v2_4_15.Equipment.ProtectedSwitch import ProtectedSwitch


class LoadBreakSwitch(ProtectedSwitch):
	'''
	A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions.

		'''

	

	__doc__ += '\n Documentation of parent class ProtectedSwitch: \n' + ProtectedSwitch.__doc__ 

	def __init__(self,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		pass
	
	def __str__(self):
		str = 'class=LoadBreakSwitch\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
