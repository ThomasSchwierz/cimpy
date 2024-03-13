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
class UnderexcLimIEEE2(UnderexcitationLimiterDynamics):
    """
    The class represents the Type UEL2 which has either a straight-line or multi-segment characteristic when plotted in
      terms of machine reactive power output vs. real power output.  Reference: IEEE UEL2 421.5-2005 Section 10.2.
      (Limit characteristic lookup table shown in Figure 10.4 (p 32) of the standard).

    tuv: Voltage filter time constant (T).  Typical Value = 5.
    tup: Real power filter time constant (T).  Typical Value = 5.
    tuq: Reactive power filter time constant (T).  Typical Value = 0.
    kui: UEL integral gain (K).  Typical Value = 0.5.
    kul: UEL proportional gain (K).  Typical Value = 0.8.
    vuimax: UEL integrator output maximum limit (V).  Typical Value = 0.25.
    vuimin: UEL integrator output minimum limit (V).  Typical Value = 0.
    kuf: UEL excitation system stabilizer gain (K).  Typical Value = 0.
    kfb: Gain associated with optional integrator feedback input signal to UEL (K).  Typical Value = 0.
    tul: Time constant associated with optional integrator feedback input signal to UEL (T).  Typical Value = 0.
    tu1: UEL lead time constant (T).  Typical Value = 0.
    tu2: UEL lag time constant (T).  Typical Value = 0.
    tu3: UEL lead time constant (T).  Typical Value = 0.
    tu4: UEL lag time constant (T).  Typical Value = 0.
    vulmax: UEL output maximum limit (V).  Typical Value = 0.25.
    vulmin: UEL output minimum limit (V).  Typical Value = 0.
    p0: Real power values for endpoints (P).  Typical Value = 0.
    q0: Reactive power values for endpoints (Q).  Typical Value = -0.31.
    p1: Real power values for endpoints (P).  Typical Value = 0.3.
    q1: Reactive power values for endpoints (Q).  Typical Value = -0.31.
    p2: Real power values for endpoints (P).  Typical Value = 0.6.
    q2: Reactive power values for endpoints (Q).  Typical Value = -0.28.
    p3: Real power values for endpoints (P).  Typical Value = 0.9.
    q3: Reactive power values for endpoints (Q).  Typical Value = -0.21.
    p4: Real power values for endpoints (P).  Typical Value = 1.02.
    q4: Reactive power values for endpoints (Q).  Typical Value = 0.
    p5: Real power values for endpoints (P).
    q5: Reactive power values for endpoints (Q).
    p6: Real power values for endpoints (P).
    q6: Reactive power values for endpoints (Q).
    p7: Real power values for endpoints (P).
    q7: Reactive power values for endpoints (Q).
    p8: Real power values for endpoints (P).
    q8: Reactive power values for endpoints (Q).
    p9: Real power values for endpoints (P).
    q9: Reactive power values for endpoints (Q).
    p10: Real power values for endpoints (P).
    q10: Reactive power values for endpoints (Q).
    k1: UEL terminal voltage exponent applied to real power input to UEL limit look-up table (k1).  Typical Value = 2.
    k2: UEL terminal voltage exponent applied to reactive power output from UEL limit look-up table (k2).  Typical Value
      = 2.
    """

    tuv : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tup : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tuq : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kui : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kul : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vuimax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vuimin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kuf : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kfb : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tul : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tu1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tu2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tu3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tu4 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vulmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vulmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    p0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    q0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    p1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    q1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    p2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    q2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    p3 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    q3 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    p4 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    q4 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    p5 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    q5 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    p6 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    q6 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    p7 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    q7 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    p8 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    q8 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    p9 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    q9 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    p10 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    q10 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
