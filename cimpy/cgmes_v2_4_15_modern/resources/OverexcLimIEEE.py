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
class OverexcLimIEEE(OverexcitationLimiterDynamics):
    """
    The over excitation limiter model is intended to represent the significant features of OELs necessary for some
      large-scale system studies. It is the result of a pragmatic approach to obtain a model that can be widely
      applied with attainable data from generator owners. An attempt to include all variations in the functionality
      of OELs and duplicate how they interact with the rest of the excitation systems would likely result in a level
      of application insufficient for the studies for which they are intended.  Reference: IEEE OEL 421.5-2005
      Section 9.

    itfpu: OEL timed field current limiter pickup level (I).  Typical Value = 1.05.
    ifdmax: OEL instantaneous field current limit (I).  Typical Value = 1.5.
    ifdlim: OEL timed field current limit (I).  Typical Value = 1.05.
    hyst: OEL pickup/drop-out hysteresis (HYST).  Typical Value = 0.03.
    kcd: OEL cooldown gain (K).  Typical Value = 1.
    kramp: OEL ramped limit rate (K).  Unit = PU/sec.  Typical Value = 10.
    """

    itfpu : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ifdmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ifdlim : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    hyst : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kcd : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kramp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
