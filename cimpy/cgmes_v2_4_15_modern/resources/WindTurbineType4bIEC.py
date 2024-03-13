"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .WindGenType4IEC import WindGenType4IEC

@dataclass
class WindTurbineType4bIEC(WindGenType4IEC):
    """
    Wind turbine IEC Type 4A.  Reference: IEC Standard 61400-27-1, section 6.5.5.3.

    WindContPType4bIEC: Wind control P type 4B model associated with this wind turbine type 4B model.
    WindMechIEC: Wind mechanical model associated with this wind turbine Type 4B model.
    """

    WindContPType4bIEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    WindMechIEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
