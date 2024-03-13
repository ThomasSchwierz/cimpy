"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from ..utils.base import Base

@dataclass
class Voltage(Base):
    """
    Electrical voltage, can be both AC and DC.

    value: 
    unit: 
    multiplier: 
    """

    value : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, Profile.SV, Profile.EQ_BD, Profile.SSH, ]}) 

    unit : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, Profile.SV, Profile.EQ_BD, Profile.SSH, ]}) 

    multiplier : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, Profile.SV, Profile.EQ_BD, Profile.SSH, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ, Profile.SV, Profile.EQ_BD, Profile.SSH,  }
