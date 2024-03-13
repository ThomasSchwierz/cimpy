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
class MeasurementValue(IdentifiedObject):
    """
    The current state for a measurement. A state value is an instance of a measurement from a specific source.
      Measurements can be associated with many state values, each representing a different source for the
      measurement.

    timeStamp: The time when the value was last updated
    sensorAccuracy: The limit, expressed as a percentage of the sensor maximum, that errors will not exceed when the
      sensor is used under  reference conditions.
    MeasurementValueQuality: A MeasurementValue has a MeasurementValueQuality associated with it.
    MeasurementValueSource: The MeasurementValues updated by the source.
    """

    timeStamp : str = Field(default="", json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    sensorAccuracy : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    # *Association not used*
    # Type M:0..1 in CIM
    # MeasurementValueQuality : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    MeasurementValueSource : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
