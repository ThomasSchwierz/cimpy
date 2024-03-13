"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .GeneratingUnit import GeneratingUnit

@dataclass
class HydroGeneratingUnit(GeneratingUnit):
    """
    A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan).

    energyConversionCapability: Energy conversion capability for generating.
    HydroPowerPlant: The hydro generating unit belongs to a hydro power plant.
    """

    energyConversionCapability : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    HydroPowerPlant : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ, Profile.SSH,  }
