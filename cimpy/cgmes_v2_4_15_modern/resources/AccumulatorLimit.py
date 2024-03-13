"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .Limit import Limit

@dataclass
class AccumulatorLimit(Limit):
    """
    Limit values for Accumulator measurements.

    value: The value to supervise against. The value is positive.
    LimitSet: The limit values used for supervision of Measurements.
    """

    value : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    LimitSet : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
