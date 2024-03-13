"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .MeasurementValue import MeasurementValue

@dataclass
class AnalogValue(MeasurementValue):
    """
    AnalogValue represents an analog MeasurementValue.

    Analog: The values connected to this measurement.
    AnalogControl: The MeasurementValue that is controlled.
    value: The value to supervise.
    """

    Analog : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    # *Association not used*
    # Type M:0..1 in CIM
    # AnalogControl : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    value : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
