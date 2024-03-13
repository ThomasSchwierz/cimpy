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
class OverexcLimX2(OverexcitationLimiterDynamics):
    """
    Field Voltage or Current overexcitation limiter designed to protect the generator field of an AC machine with
      automatic excitation control from overheating due to prolonged overexcitation.

    m: (m). true = IFD limiting false = EFD limiting.
    efdrated: Rated field voltage if m=F or field current if m=T (EFD).  Typical Value = 1.05.
    efd1: Low voltage or current point on the inverse time characteristic (EFD).  Typical Value = 1.1.
    t1: Time to trip the exciter at the low voltage or current point on the inverse time characteristic (TIME).  Typical
      Value = 120.
    efd2: Mid voltage or current point on the inverse time characteristic (EFD).  Typical Value = 1.2.
    t2: Time to trip the exciter at the mid voltage or current point on the inverse time characteristic (TIME).  Typical
      Value = 40.
    efd3: High voltage or current point on the inverse time characteristic (EFD).  Typical Value = 1.5.
    t3: Time to trip the exciter at the high voltage or current point on the inverse time characteristic (TIME).
      Typical Value = 15.
    efddes: Desired field voltage if m=F or field current if m=T (EFD).  Typical Value = 1.
    kmx: Gain (K).  Typical Value = 0.002.
    vlow: Low voltage limit (V) (>0).
    """

    m : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efdrated : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efd1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efd2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efd3 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efddes : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kmx : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vlow : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
