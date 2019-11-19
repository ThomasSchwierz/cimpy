from cimpy.cimgen_v2_4_15.Base import Base


class ConnectivityNode(Base):
	'''
	Connectivity nodes are points where terminals of AC conducting equipment are connected together with zero impedance.

	:TopologicalNode: The connectivity nodes combine together to form this topological node.  May depend on the current state of switches in the network. Default: None
		'''

	

	

	def __init__(self, TopologicalNode = None,  ):
	
		self.TopologicalNode = TopologicalNode
		
	def __str__(self):
		str = 'class=ConnectivityNode\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
