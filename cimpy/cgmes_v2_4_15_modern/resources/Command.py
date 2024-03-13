"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .Control import Control

@dataclass
class Command(Control):
    """
    A Command is a discrete control used for supervisory control.

    normalValue: Normal value for Control.value e.g. used for percentage scaling.
    value: The value representing the actuator output.
    DiscreteValue: The Control variable associated with the MeasurementValue.
    ValueAliasSet: The ValueAliasSet used for translation of a Control value to a name.
    """

    normalValue : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    value : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    DiscreteValue : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    ValueAliasSet : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
