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
class PssPTIST1(PowerSystemStabilizerDynamics):
    """
    PTI Microprocessor-Based Stabilizer type 1.

    m: (M).  M=2*H.  Typical Value = 5.
    tf: Time constant (Tf).  Typical Value = 0.2.
    tp: Time constant (Tp).  Typical Value = 0.2.
    t1: Time constant (T1).  Typical Value = 0.3.
    t2: Time constant (T2).  Typical Value = 1.
    t3: Time constant (T3).  Typical Value = 0.2.
    t4: Time constant (T4).  Typical Value = 0.05.
    k: Gain (K).  Typical Value = 9.
    dtf: Time step frequency calculation (Dtf).  Typical Value = 0.025.
    dtc: Time step related to activation of controls (Dtc).  Typical Value = 0.025.
    dtp: Time step active power calculation (Dtp).  Typical Value = 0.0125.
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



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
