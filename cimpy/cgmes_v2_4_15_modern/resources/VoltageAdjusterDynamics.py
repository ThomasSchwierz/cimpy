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
class VoltageAdjusterDynamics(DynamicsFunctionBlock):
    """
    Voltage adjuster function block whose behaviour is described by reference to a standard model

    PFVArControllerType1Dynamics: Power Factor or VAr controller Type I model with which this voltage adjuster is
      associated.
    """

    PFVArControllerType1Dynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
