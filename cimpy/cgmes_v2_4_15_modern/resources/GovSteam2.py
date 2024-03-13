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
class GovSteam2(TurbineGovernorDynamics):
    """
    Simplified governor model.

    k: Governor gain (reciprocal of droop) (K).  Typical Value = 20.
    dbf: Frequency dead band (DBF).  Typical Value = 0.
    t1: Governor lag time constant (T) (>0).  Typical Value = 0.45.
    t2: Governor lead time constant (T) (may be 0).  Typical Value = 0.
    pmax: Maximum fuel flow (P).  Typical Value = 1.
    pmin: Minimum fuel flow (P).  Typical Value = 0.
    mxef: Fuel flow maximum positive error value (MX).  Typical Value = 1.
    mnef: Fuel flow maximum negative error value (MN).  Typical Value = -1.
    """

    k : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    dbf : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    mxef : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    mnef : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
