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
class GovSteamCC(TurbineGovernorDynamics):
    """
    Cross compound turbine governor model.

    mwbase: Base for power values (MWbase) (>0).  Unit = MW.
    pmaxhp: Maximum HP value position (Pmaxhp).  Typical Value = 1.
    rhp: HP governor droop (Rhp).  Typical Value = 0.05.
    t1hp: HP governor time constant (T1hp).  Typical Value = 0.1.
    t3hp: HP turbine time constant (T3hp).  Typical Value = 0.1.
    t4hp: HP turbine time constant (T4hp).  Typical Value = 0.1.
    t5hp: HP reheater time constant (T5hp).  Typical Value = 10.
    fhp: Fraction of HP power ahead of reheater (Fhp).  Typical Value = 0.3.
    dhp: HP damping factor (Dhp).  Typical Value = 0.
    pmaxlp: Maximum LP value position (Pmaxlp).  Typical Value = 1.
    rlp: LP governor droop (Rlp).  Typical Value = 0.05.
    t1lp: LP governor time constant (T1lp).  Typical Value = 0.1.
    t3lp: LP turbine time constant (T3lp).  Typical Value = 0.1.
    t4lp: LP turbine time constant (T4lp).  Typical Value = 0.1.
    t5lp: LP reheater time constant (T5lp).  Typical Value = 10.
    flp: Fraction of LP power ahead of reheater (Flp).  Typical Value = 0.7.
    dlp: LP damping factor (Dlp).  Typical Value = 0.
    """

    mwbase : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmaxhp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rhp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t1hp : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t3hp : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t4hp : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t5hp : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    fhp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    dhp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmaxlp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rlp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t1lp : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t3lp : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t4lp : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t5lp : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    flp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    dlp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
