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
class WindGenTurbineType3aIEC(WindGenTurbineType3IEC):
    """
    IEC Type 3A generator set model.  Reference: IEC Standard 61400-27-1 Section 6.6.3.2.

    kpc: Current PI controller proportional gain (K). It is type dependent parameter.
    xs: Electromagnetic transient reactance (x). It is type dependent parameter.
    tic: Current PI controller integration time constant (T). It is type dependent parameter.
    """

    kpc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    xs : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tic : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
