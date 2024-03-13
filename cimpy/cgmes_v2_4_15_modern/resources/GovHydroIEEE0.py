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
class GovHydroIEEE0(TurbineGovernorDynamics):
    """
    IEEE Simplified Hydro Governor-Turbine Model.  Used for Mechanical-Hydraulic and Electro-Hydraulic turbine
      governors, with our without steam feedback. Typical values given are for Mechanical-Hydraulic.  Ref

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    k: Governor gain (K.
    t1: Governor lag time constant (T1).  Typical Value = 0.25.
    t2: Governor lead time constant (T2.  Typical Value = 0.
    t3: Gate actuator time constant (T3).  Typical Value = 0.1.
    t4: Water starting time (T4).
    pmax: Gate maximum (Pmax).
    pmin: Gate minimum (Pmin).
    """

    mwbase : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t4 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
