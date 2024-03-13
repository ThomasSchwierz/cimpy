"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .PowerSystemResource import PowerSystemResource

@dataclass
class ConnectivityNodeContainer(PowerSystemResource):
    """
    A base class for all objects that may contain connectivity nodes or topological nodes.

    ConnectivityNodes: Connectivity nodes which belong to this connectivity node container.
    TopologicalNode: The topological nodes which belong to this connectivity node container.
    """

    # *Association not used*
    # Type M:0..n in CIM
    # ConnectivityNodes : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, Profile.EQ_BD, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..n in CIM
    # TopologicalNode : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.TP_BD, Profile.TP, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ, Profile.EQ_BD, Profile.TP_BD, Profile.TP,  }
