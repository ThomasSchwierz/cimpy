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
class GovSteamFV3(TurbineGovernorDynamics):
    """
    Simplified GovSteamIEEE1 Steam turbine governor model with Prmax limit and fast valving.

    mwbase: Base for power values (MWbase) (>0).  Unit = MW.
    k: Governor gain, (reciprocal of droop) (K).  Typical Value = 20.
    t1: Governor lead time constant (T1).  Typical Value = 0.
    t2: Governor lag time constant (T2).  Typical Value = 0.
    t3: Valve positioner time constant (T3).  Typical Value = 0.
    uo: Maximum valve opening velocity (Uo).  Unit = PU/sec.  Typical Value = 0.1.
    uc: Maximum valve closing velocity (Uc).  Unit = PU/sec.  Typical Value = -1.
    pmax: Maximum valve opening, PU of MWbase (Pmax).  Typical Value = 1.
    pmin: Minimum valve opening, PU of MWbase (Pmin).  Typical Value = 0.
    t4: Inlet piping/steam bowl time constant (T4).  Typical Value = 0.2.
    k1: Fraction of turbine power developed after first boiler pass (K1).  Typical Value = 0.2.
    t5: Time constant of second boiler pass (i.e. reheater) (T5).  Typical Value = 0.5.
    k2: Fraction of turbine power developed after second boiler pass (K2).  Typical Value = 0.2.
    t6: Time constant of crossover or third boiler pass (T6).  Typical Value = 10.
    k3: Fraction of hp turbine power developed after crossover or third boiler pass (K3). Typical Value = 0.6.
    ta: Time to close intercept valve (IV) (Ta).  Typical Value = 0.97.
    tb: Time until IV starts to reopen (Tb).  Typical Value = 0.98.
    tc: Time until IV is fully open (Tc).  Typical Value = 0.99.
    prmax: Max. pressure in reheater (Prmax).  Typical Value = 1.
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

    t5 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t6 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k3 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tb : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    prmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
