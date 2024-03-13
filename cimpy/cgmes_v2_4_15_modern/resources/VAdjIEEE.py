"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .VoltageAdjusterDynamics import VoltageAdjusterDynamics

@dataclass
class VAdjIEEE(VoltageAdjusterDynamics):
    """
    The class represents IEEE Voltage Adjuster which is used to represent the voltage adjuster in either a power factor
      or var control system.  Reference: IEEE Standard 421.5-2005 Section 11.1.

    vadjf: Set high to provide a continuous raise or lower ().
    adjslew: Rate at which output of adjuster changes ().  Unit = sec./PU.  Typical Value = 300.
    vadjmax: Maximum output of the adjuster ().  Typical Value = 1.1.
    vadjmin: Minimum output of the adjuster ().  Typical Value = 0.9.
    taon: Time that adjuster pulses are on ().  Typical Value = 0.1.
    taoff: Time that adjuster pulses are off ().  Typical Value = 0.5.
    """

    vadjf : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    adjslew : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vadjmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vadjmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    taon : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    taoff : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
