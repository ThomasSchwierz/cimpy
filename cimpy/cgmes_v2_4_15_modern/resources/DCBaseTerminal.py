"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .ACDCTerminal import ACDCTerminal

@dataclass
class DCBaseTerminal(ACDCTerminal):
    """
    An electrical connection point at a piece of DC conducting equipment. DC terminals are connected at one physical DC
      node that may have multiple DC terminals connected. A DC node is similar to an AC connectivity node. The model
      enforces that DC connections are distinct from AC connections.

    DCNode: 
    DCTopologicalNode: See association end TopologicalNode.Terminal.
    """

    DCNode : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    DCTopologicalNode : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.TP, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ, Profile.SSH, Profile.TP,  }
