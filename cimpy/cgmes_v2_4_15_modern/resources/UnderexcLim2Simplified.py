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
class UnderexcLim2Simplified(UnderexcitationLimiterDynamics):
    """
    This model can be derived from UnderexcLimIEEE2. The limit characteristic (look -up table) is a single straight-
      line, the same as UnderexcLimIEEE2 (see Figure 10.4 (p 32), IEEE 421.5-2005 Section 10.2).

    q0: Segment Q initial point (Q0).  Typical Value = -0.31.
    q1: Segment Q end point (Q1).  Typical Value = -0.1.
    p0: Segment P initial point (P0).  Typical Value = 0.
    p1: Segment P end point (P1).  Typical Value = 1.
    kui: Gain Under excitation limiter (Kui).  Typical Value = 0.1.
    vuimin: Minimum error signal (V).  Typical Value = 0.
    vuimax: Maximum error signal (V).  Typical Value = 1.
    """

    q0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    q1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    p0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    p1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kui : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vuimin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vuimax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
