"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .VoltageCompensatorDynamics import VoltageCompensatorDynamics

@dataclass
class VCompIEEEType2(VoltageCompensatorDynamics):
    """
    

    tr: 
    GenICompensationForGenJ: Compensation of this voltage compensator`s generator for current flow out of another
      generator.
    """

    tr : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    # *Association not used*
    # Type M:2..n in CIM
    # GenICompensationForGenJ : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
