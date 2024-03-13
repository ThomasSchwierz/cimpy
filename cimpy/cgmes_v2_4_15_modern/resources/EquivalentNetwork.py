"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .ConnectivityNodeContainer import ConnectivityNodeContainer

@dataclass
class EquivalentNetwork(ConnectivityNodeContainer):
    """
    A class that represents an external meshed network that has been reduced to an electrically equivalent model. The
      ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The
      boundary Connectivity nodes where the equivalent connects outside itself are NOT contained by the equivalent.

    EquivalentEquipments: The equivalent where the reduced model belongs.
    """

    # *Association not used*
    # Type M:0..n in CIM
    # EquivalentEquipments : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
