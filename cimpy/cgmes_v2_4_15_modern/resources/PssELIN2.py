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
class PssELIN2(PowerSystemStabilizerDynamics):
    """
    Power system stabilizer typically associated with ExcELIN2 (though PssIEEE2B or Pss2B can also be used).

    ts1: Time constant (Ts1).  Typical Value = 0.
    ts2: Time constant (Ts2).  Typical Value = 1.
    ts3: Time constant (Ts3).  Typical Value = 1.
    ts4: Time constant (Ts4).  Typical Value = 0.1.
    ts5: Time constant (Ts5).  Typical Value = 0.
    ts6: Time constant (Ts6).  Typical Value = 1.
    ks1: Gain (Ks1).  Typical Value = 1.
    ks2: Gain (Ks2).  Typical Value = 0.1.
    ppss: Coefficient (p_PSS) (>=0 and <=4).  Typical Value = 0.1.
    apss: Coefficient (a_PSS).  Typical Value = 0.1.
    psslim: PSS limiter (psslim).  Typical Value = 0.1.
    """

    ts1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ts2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ts3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ts4 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ts5 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ts6 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ks1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ks2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ppss : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    apss : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    psslim : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
