"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .AnalogControl import AnalogControl

@dataclass
class SetPoint(AnalogControl):
    """
    An analog control that issue a set point value.

    normalValue: Normal value for Control.value e.g. used for percentage scaling.
    value: The value representing the actuator output.
    """

    normalValue : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    value : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
