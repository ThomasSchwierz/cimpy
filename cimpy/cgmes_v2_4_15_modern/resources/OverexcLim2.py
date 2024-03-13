"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .OverexcitationLimiterDynamics import OverexcitationLimiterDynamics

@dataclass
class OverexcLim2(OverexcitationLimiterDynamics):
    """
    Different from LimIEEEOEL, LimOEL2 has a fixed pickup threshold and reduces the excitation set-point by mean of non-
      windup integral regulator. Irated is the rated machine excitation current (calculated from nameplate
      conditions: V, P, CosPhi).

    koi: Gain Over excitation limiter (K).  Typical Value = 0.1.
    voimax: Maximum error signal (V).  Typical Value = 0.
    voimin: Minimum error signal (V).  Typical Value = -9999.
    ifdlim: Limit value of rated field current (I).  Typical Value = 1.05.
    """

    koi : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    voimax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    voimin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ifdlim : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
