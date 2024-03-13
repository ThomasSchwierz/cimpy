"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .LimitSet import LimitSet

@dataclass
class AccumulatorLimitSet(LimitSet):
    """
    An AccumulatorLimitSet specifies a set of Limits that are associated with an Accumulator measurement.

    Measurements: A measurement may have zero or more limit ranges defined for it.
    Limits: The set of limits.
    """

    Measurements : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    # *Association not used*
    # Type M:1..n in CIM
    # Limits : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
