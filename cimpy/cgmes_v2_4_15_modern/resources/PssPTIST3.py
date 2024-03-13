"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics

@dataclass
class PssPTIST3(PowerSystemStabilizerDynamics):
    """
    PTI Microprocessor-Based Stabilizer type 3.

    m: (M).  M=2*H.  Typical Value = 5.
    tf: Time constant (Tf).  Typical Value = 0.2.
    tp: Time constant (Tp).  Typical Value = 0.2.
    t1: Time constant (T1).  Typical Value = 0.3.
    t2: Time constant (T2).  Typical Value = 1.
    t3: Time constant (T3).  Typical Value = 0.2.
    t4: Time constant (T4).  Typical Value = 0.05.
    k: Gain (K).  Typical Value = 9.
    dtf: Time step frequency calculation (0.03 for 50 Hz) (Dtf).  Typical Value = 0.025.
    dtc: Time step related to activation of controls (0.03 for 50 Hz) (Dtc).  Typical Value = 0.025.
    dtp: Time step active power calculation (0.015 for 50 Hz) (Dtp).  Typical Value = 0.0125.
    t5: Time constant (T5).
    t6: Time constant (T6).
    a0: Filter coefficient (A0).
    a1: Limiter (Al).
    a2: Filter coefficient (A2).
    b0: Filter coefficient (B0).
    b1: Filter coefficient (B1).
    b2: Filter coefficient (B2).
    a3: Filter coefficient (A3).
    a4: Filter coefficient (A4).
    a5: Filter coefficient (A5).
    b3: Filter coefficient (B3).
    b4: Filter coefficient (B4).
    b5: Filter coefficient (B5).
    athres: Threshold value above which output averaging will be bypassed (Athres).  Typical Value = 0.005.
    dl: Limiter (Dl).
    al: Limiter (Al).
    lthres: Threshold value (Lthres).
    pmin: (Pmin).
    isw: Digital/analog output switch (Isw). true = produce analog output false = convert to digital output, using tap
      selection table.
    nav: Number of control outputs to average (Nav) (1 <= Nav <= 16).  Typical Value = 4.
    ncl: Number of counts at limit to active limit function (Ncl) (>0).
    ncr: Number of counts until reset after limit function is triggered (Ncr).
    """

    m : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tf : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tp : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t4 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    dtf : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    dtc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    dtp : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t5 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t6 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    a0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    a1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    a2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    b0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    b1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    b2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    a3 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    a4 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    a5 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    b3 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    b4 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    b5 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    athres : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    dl : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    al : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    lthres : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    isw : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    nav : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ncl : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ncr : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
