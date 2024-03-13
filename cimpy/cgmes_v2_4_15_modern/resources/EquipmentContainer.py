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
class EquipmentContainer(ConnectivityNodeContainer):
    """
    A modeling construct to provide a root class for containing equipment.

    Equipments: Contained equipment.
    """

    # *Association not used*
    # Type M:0..n in CIM
    # Equipments : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, Profile.EQ_BD, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ, Profile.EQ_BD,  }
