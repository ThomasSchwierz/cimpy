"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .DynamicsFunctionBlock import DynamicsFunctionBlock

@dataclass
class WindTurbineType3or4Dynamics(DynamicsFunctionBlock):
    """
    Parent class supporting relationships to wind turbines Type 3 and 4 and wind plant including their control models.

    EnergySource: Energy Source (current source) with which this wind Type 3 or 4 dynamics model is asoociated.
    RemoteInputSignal: Wind turbine Type 3 or 4 models using this remote input signal.
    WindPlantDynamics: The wind plant with which the wind turbines type 3 or 4 are associated.
    """

    EnergySource : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    RemoteInputSignal : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    WindPlantDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
