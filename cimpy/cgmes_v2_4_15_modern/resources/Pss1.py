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
class Pss1(PowerSystemStabilizerDynamics):
    """
    Italian PSS - three input PSS (speed, frequency, power).

    kw: Shaft speed power input gain (K).  Typical Value = 0.
    kf: Frequency power input gain (K).  Typical Value = 5.
    kpe: Electric power input gain (K).  Typical Value = 0.3.
    pmin: Minimum power PSS enabling (P).  Typical Value = 0.25.
    ks: PSS gain (K).  Typical Value = 1.
    vsmn: Stabilizer output max limit (V).  Typical Value = -0.06.
    vsmx: Stabilizer output min limit (V).  Typical Value = 0.06.
    tpe: Electric power filter time constant (T).  Typical Value = 0.05.
    t5: Washout (T).  Typical Value = 3.5.
    t6: Filter time constant (T).  Typical Value = 0.
    t7: Lead/lag time constant (T).  Typical Value = 0.
    t8: Lead/lag time constant (T).  Typical Value = 0.
    t9: Lead/lag time constant (T).  Typical Value = 0.
    t10: Lead/lag time constant (T).  Typical Value = 0.
    vadat: 
    """

    kw : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kf : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kpe : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ks : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vsmn : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vsmx : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tpe : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t5 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t6 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t7 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t8 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t9 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t10 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vadat : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
