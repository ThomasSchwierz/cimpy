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
class PssSH(PowerSystemStabilizerDynamics):
    """
    Model for Siemens "H infinity" power system stabilizer with generator electrical power input.

    k: Main gain (K).  Typical Value = 1.
    k0: Gain 0 (K0).  Typical Value = 0.012.
    k1: Gain 1 (K1).  Typical Value = 0.488.
    k2: Gain 2 (K2).  Typical Value = 0.064.
    k3: Gain 3 (K3).  Typical Value = 0.224.
    k4: Gain 4 (K4).  Typical Value = 0.1.
    td: Input time constant (Td).  Typical Value = 10.
    t1: Time constant 1 (T1).  Typical Value = 0.076.
    t2: Time constant 2 (T2).  Typical Value = 0.086.
    t3: Time constant 3 (T3).   Typical Value = 1.068.
    t4: Time constant 4 (T4).  Typical Value = 1.913.
    vsmax: Output maximum limit (Vsmax).  Typical Value = 0.1.
    vsmin: Output minimum limit (Vsmin).  Typical Value = -0.1.
    """

    k : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k3 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k4 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    td : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t4 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vsmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vsmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
