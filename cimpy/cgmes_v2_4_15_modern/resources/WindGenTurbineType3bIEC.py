"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .WindGenTurbineType3IEC import WindGenTurbineType3IEC

@dataclass
class WindGenTurbineType3bIEC(WindGenTurbineType3IEC):
    """
    IEC Type 3B generator set model.  Reference: IEC Standard 61400-27-1 Section 6.6.3.3.

    fducw: Crowbar duration versus voltage variation look-up table (f()). It is case dependent parameter.
    tg: Current generation Time constant (). It is type dependent parameter.
    two: Time constant for crowbar washout filter (). It is case dependent parameter.
    mwtcwp: Crowbar control mode ().   The parameter is case dependent parameter.
    xs: Electromagnetic transient reactance (x). It is type dependent parameter.
    """

    fducw : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tg : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    two : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    mwtcwp : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    xs : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
