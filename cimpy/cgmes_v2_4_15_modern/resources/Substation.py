"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .EquipmentContainer import EquipmentContainer

@dataclass
class Substation(EquipmentContainer):
    """
    A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk
      is passed for the purposes of switching or modifying its characteristics.

    DCConverterUnit: 
    Region: The SubGeographicalRegion containing the substation.
    VoltageLevels: The voltage levels within this substation.
    """

    # *Association not used*
    # Type M:0..n in CIM
    # DCConverterUnit : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    Region : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    # *Association not used*
    # Type M:0..n in CIM
    # VoltageLevels : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
