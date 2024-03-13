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
class GovGAST4(TurbineGovernorDynamics):
    """
    Generic turbogas.

    bp: Droop (bp).  Typical Value = 0.05.
    tv: Time constant of fuel valve positioner (T).  Typical Value = 0.1.
    ta: Maximum gate opening velocity (T).  Typical Value = 3.
    tc: Maximum gate closing velocity (T).  Typical Value = 0.5.
    tcm: Fuel control time constant (T).  Typical Value = 0.1.
    ktm: Compressor gain (K).  Typical Value = 0.
    tm: Compressor discharge volume time constant (T).  Typical Value = 0.2.
    rymx: Maximum valve opening (RYMX).  Typical Value = 1.1.
    rymn: Minimum valve opening (RYMN).  Typical Value = 0.
    mxef: Fuel flow maximum positive error value (MX).  Typical Value = 0.05.
    mnef: Fuel flow maximum negative error value (MN).  Typical Value = -0.05.
    """

    bp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tv : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tcm : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ktm : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tm : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rymx : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rymn : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    mxef : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    mnef : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
