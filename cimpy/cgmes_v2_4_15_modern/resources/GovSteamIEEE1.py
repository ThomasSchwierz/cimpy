"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovSteamIEEE1(TurbineGovernorDynamics):
    """
    IEEE steam turbine governor model.  Ref

    mwbase: Base for power values (MWbase) (> 0)
    k: Governor gain (reciprocal of droop) (K) (> 0).  Typical Value = 25.
    t1: Governor lag time constant (T1).  Typical Value = 0.
    t2: Governor lead time constant (T2).  Typical Value = 0.
    t3: Valve positioner time constant (T3) (> 0).  Typical Value = 0.1.
    uo: Maximum valve opening velocity (Uo) (> 0).  Unit = PU/sec.  Typical Value = 1.
    uc: Maximum valve closing velocity (Uc) (< 0).  Unit = PU/sec.  Typical Value = -10.
    pmax: Maximum valve opening (Pmax) (> Pmin).  Typical Value = 1.
    pmin: Minimum valve opening (Pmin) (>= 0).  Typical Value = 0.
    t4: Inlet piping/steam bowl time constant (T4).  Typical Value = 0.3.
    k1: Fraction of HP shaft power after first boiler pass (K1).  Typical Value = 0.2.
    k2: Fraction of LP shaft power after first boiler pass (K2).  Typical Value = 0.
    t5: Time constant of second boiler pass (T5).  Typical Value = 5.
    k3: Fraction of HP shaft power after second boiler pass (K3).  Typical Value = 0.3.
    k4: Fraction of LP shaft power after second boiler pass (K4).  Typical Value = 0.
    t6: Time constant of third boiler pass (T6).  Typical Value = 0.5.
    k5: Fraction of HP shaft power after third boiler pass (K5).  Typical Value = 0.5.
    k6: Fraction of LP shaft power after third boiler pass (K6).  Typical Value = 0.
    t7: Time constant of fourth boiler pass (T7).  Typical Value = 0.
    k7: Fraction of HP shaft power after fourth boiler pass (K7).  Typical Value = 0.
    k8: Fraction of LP shaft power after fourth boiler pass (K8).  Typical Value = 0.
    """

    mwbase : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    uo : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    uc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t4 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t5 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k3 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k4 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t6 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k5 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k6 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t7 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k7 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k8 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
