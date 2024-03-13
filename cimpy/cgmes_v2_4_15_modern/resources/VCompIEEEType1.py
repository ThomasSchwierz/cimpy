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
class VCompIEEEType1(VoltageCompensatorDynamics):
    """
    Reference: IEEE Standard 421.5-2005 Section 4.

    rc: 
    xc: 
    tr: 
    """

    rc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    xc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tr : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
