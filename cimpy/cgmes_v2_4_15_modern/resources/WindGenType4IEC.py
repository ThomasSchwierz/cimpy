"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .WindTurbineType3or4IEC import WindTurbineType3or4IEC

@dataclass
class WindGenType4IEC(WindTurbineType3or4IEC):
    """
    IEC Type 4 generator set model.  Reference: IEC Standard 61400-27-1 Section 6.6.3.4.

    dipmax: Maximum active current ramp rate (di). It is project dependent parameter.
    diqmin: Minimum reactive current ramp rate (d). It is case dependent parameter.
    diqmax: Maximum reactive current ramp rate (di). It is project dependent parameter.
    tg: Time constant (T). It is type dependent parameter.
    """

    dipmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    diqmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    diqmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tg : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
