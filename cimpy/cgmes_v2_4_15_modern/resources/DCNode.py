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
class DCNode(IdentifiedObject):
    """
    DC nodes are points where terminals of DC conducting equipment are connected together with zero impedance.

    DCTerminals: 
    DCEquipmentContainer: 
    DCTopologicalNode: See association end TopologicalNode.ConnectivityNodes.
    """

    # *Association not used*
    # Type M:0..n in CIM
    # DCTerminals : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    DCEquipmentContainer : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    DCTopologicalNode : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.TP, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ, Profile.TP,  }
