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
class GovSteamFV2(TurbineGovernorDynamics):
    """
    Steam turbine governor with reheat time constants and modeling of the effects of fast valve closing to reduce
      mechanical power.

    mwbase: Alternate Base used instead of Machine base in equipment model if necessary (MWbase) (>0).  Unit = MW.
    r: (R).
    t1: Governor time constant (T1).
    vmax: (Vmax).
    vmin: (Vmin).
    k: Fraction of the turbine power developed by turbine sections not involved in fast valving (K).
    t3: Reheater time constant (T3).
    dt: (Dt).
    tt: Time constant with which power falls off after intercept valve closure (Tt).
    ta: Time after initial time for valve to close (Ta).
    tb: Time after initial time for valve to begin opening (Tb).
    tc: Time after initial time for valve to become fully open (Tc).
    ti: Initial time to begin fast valving (Ti).
    """

    mwbase : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    r : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    dt : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tt : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tb : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ti : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
