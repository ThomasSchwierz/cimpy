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
class Pss5(PowerSystemStabilizerDynamics):
    """
    Italian PSS - Detailed PSS.

    kpe: Electric power input gain (K).  Typical Value = 0.3.
    kf: Frequency/shaft speed input gain (K).  Typical Value = 5.
    isfreq: Selector for Frequency/shaft speed input (IsFreq). true = speed false = frequency. Typical Value = true.
    kpss: PSS gain (K).  Typical Value = 1.
    ctw2: Selector for Second washout enabling (C). true = second washout filter is bypassed false = second washout
      filter in use. Typical Value = true.
    tw1: First WashOut (T).  Typical Value = 3.5.
    tw2: Second WashOut (T).  Typical Value = 0.
    tl1: Lead/lag time constant (T).  Typical Value = 0.
    tl2: Lead/lag time constant (T).  Typical Value = 0.
    tl3: Lead/lag time constant (T).  Typical Value = 0.
    tl4: Lead/lag time constant (T).  Typical Value = 0.
    vsmn: Stabilizer output max limit (V).  Typical Value = -0.1.
    vsmx: Stabilizer output min limit (V).  Typical Value = 0.1.
    tpe: Electric power filter time constant (T).  Typical Value = 0.05.
    pmm: Minimum power PSS enabling (P).  Typical Value = 0.25.
    deadband: Stabilizer output dead band (DeadBand).  Typical Value = 0.
    vadat: 
    """

    kpe : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kf : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    isfreq : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kpss : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ctw2 : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tw1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tw2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tl1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tl2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tl3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tl4 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vsmn : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vsmx : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tpe : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmm : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    deadband : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vadat : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
