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
class RegularTimePoint(Base):
    """
    Time point for a schedule where the time between the consecutive points is constant.

    IntervalSchedule: Regular interval schedule containing this time point.
    sequenceNumber: The position of the regular time point in the sequence. Note that time points don`t have to be
      sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is
      computed by multiplying the associated regular interval schedule`s time step with the regular
      time point sequence number and adding the associated schedules start time.
    value1: The first value at the time. The meaning of the value is defined by the derived type of the associated
      schedule.
    value2: The second value at the time. The meaning of the value is defined by the derived type of the associated
      schedule.
    """

    IntervalSchedule : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    sequenceNumber : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    value1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    value2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
