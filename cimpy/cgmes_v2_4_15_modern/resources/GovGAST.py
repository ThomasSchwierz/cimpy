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
class GovGAST(TurbineGovernorDynamics):
    """
    Single shaft gas turbine.

    mwbase: Base for power values (MWbase) (> 0).
    r: Permanent droop (R).  Typical Value = 0.04.
    t1: Governor mechanism time constant (T1).  T1 represents the natural valve positioning time constant of the
      governor for small disturbances, as seen when rate limiting is not in effect.  Typical Value = 0.5.
    t2: Turbine power time constant (T2).  T2 represents delay due to internal energy storage of the gas turbine engine.
      T2 can be used to give a rough approximation to the delay associated with acceleration of the compressor
      spool of a multi-shaft engine, or with the compressibility of gas in the plenum of a the free power
      turbine of an aero-derivative unit, for example.  Typical Value = 0.5.
    t3: Turbine exhaust temperature time constant (T3).  Typical Value = 3.
    at: Ambient temperature load limit (Load Limit).  Typical Value = 1.
    kt: Temperature limiter gain (Kt).  Typical Value = 3.
    vmax: Maximum turbine power, PU of MWbase (Vmax).  Typical Value = 1.
    vmin: Minimum turbine power, PU of MWbase (Vmin).  Typical Value = 0.
    dturb: Turbine damping factor (Dturb).  Typical Value = 0.18.
    """

    mwbase : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    r : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    at : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kt : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    dturb : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
