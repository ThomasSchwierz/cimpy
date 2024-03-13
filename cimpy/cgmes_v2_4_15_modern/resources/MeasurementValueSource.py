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
class MeasurementValueSource(IdentifiedObject):
    """
    MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to
      use the MeasurementValueSource attributes are described in the introduction to IEC 61970-301.

    MeasurementValues: A reference to the type of source that updates the MeasurementValue, e.g. SCADA, CCLink, manual,
      etc. User conventions for the names of sources are contained in the introduction to IEC
      61970-301.
    """

    # *Association not used*
    # Type M:0..n in CIM
    # MeasurementValues : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
