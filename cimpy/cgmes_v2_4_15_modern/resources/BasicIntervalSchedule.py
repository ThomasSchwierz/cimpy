"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .IdentifiedObject import IdentifiedObject

@dataclass
class BasicIntervalSchedule(IdentifiedObject):
    """
    Schedule of values at points in time.

    startTime: The time for the first time point.
    value1Unit: Value1 units of measure.
    value2Unit: Value2 units of measure.
    """

    startTime : str = Field(default="", json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    value1Unit : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    value2Unit : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
