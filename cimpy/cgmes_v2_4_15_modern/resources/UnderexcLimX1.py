"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics

@dataclass
class UnderexcLimX1(UnderexcitationLimiterDynamics):
    """
    

    kf2: Differential gain (Kf2).
    tf2: Differential time constant (Tf2) (>0).
    km: Minimum excitation limit gain (Km).
    tm: Minimum excitation limit time constant (Tm).
    melmax: Minimum excitation limit value (MELMAX).
    k: Minimum excitation limit slope (K) (>0).
    """

    kf2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tf2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    km : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tm : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    melmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
