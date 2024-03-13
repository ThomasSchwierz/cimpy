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
class UnderexcLimIEEE1(UnderexcitationLimiterDynamics):
    """
    The class represents the Type UEL1 model which has a circular limit boundary when plotted in terms of machine
      reactive power vs. real power output.  Reference: IEEE UEL1 421.5-2005 Section 10.1.

    kur: UEL radius setting (K).  Typical Value = 1.95.
    kuc: UEL center setting (K).  Typical Value = 1.38.
    kuf: UEL excitation system stabilizer gain (K).  Typical Value = 3.3.
    vurmax: UEL maximum limit for radius phasor magnitude (V).  Typical Value = 5.8.
    vucmax: UEL maximum limit for operating point phasor magnitude (V).  Typical Value = 5.8.
    kui: UEL integral gain (K).  Typical Value = 0.
    kul: UEL proportional gain (K).  Typical Value = 100.
    vuimax: UEL integrator output maximum limit (V).
    vuimin: UEL integrator output minimum limit (V).
    tu1: UEL lead time constant (T).  Typical Value = 0.
    tu2: UEL lag time constant (T).  Typical Value = 0.05.
    tu3: UEL lead time constant (T).  Typical Value = 0.
    tu4: UEL lag time constant (T).  Typical Value = 0.
    vulmax: UEL output maximum limit (V).  Typical Value = 18.
    vulmin: UEL output minimum limit (V).  Typical Value = -18.
    """

    kur : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kuc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kuf : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vurmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vucmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kui : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kul : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vuimax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vuimin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tu1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tu2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tu3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tu4 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vulmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vulmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
