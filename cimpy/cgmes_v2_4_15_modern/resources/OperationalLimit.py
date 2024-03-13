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
class OperationalLimit(IdentifiedObject):
    """
    A value associated with a specific kind of limit.  The sub class value attribute shall be positive.  The sub class
      value attribute is inversely proportional to OperationalLimitType.acceptableDuration (acceptableDuration for
      short). A pair of value_x and acceptableDuration_x are related to each other as follows: if value_1 > value_2
      > value_3 >... then acceptableDuration_1 < acceptableDuration_2 < acceptableDuration_3 < ... A value_x with
      direction="high" shall be greater than a value_y with direction="low".

    OperationalLimitSet: Values of equipment limits.
    OperationalLimitType: The limit type associated with this limit.
    """

    OperationalLimitSet : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    OperationalLimitType : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
