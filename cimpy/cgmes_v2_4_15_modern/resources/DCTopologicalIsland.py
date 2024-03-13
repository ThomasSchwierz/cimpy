"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .IdentifiedObject import IdentifiedObject

@dataclass
class DCTopologicalIsland(IdentifiedObject):
    """
    An electrically connected subset of the network. DC topological islands can change as the current network state
      changes: e.g. due to  - disconnect switches or breakers change state in a SCADA/EMS - manual creation, change
      or deletion of topological nodes in a planning tool.

    DCTopologicalNodes: 
    """

    DCTopologicalNodes : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.SV, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.SV,  }
