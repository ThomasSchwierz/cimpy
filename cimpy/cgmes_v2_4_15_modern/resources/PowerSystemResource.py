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
class PowerSystemResource(IdentifiedObject):
    """
    A power system resource can be an item of equipment such as a switch, an equipment container containing many
      individual items of equipment such as a substation, or an organisational entity such as sub-control area.
      Power system resources can have measurements associated.

    Controls: Regulating device governed by this control output.
    Measurements: The power system resource that contains the measurement.
    Location: Location of this power system resource.
    """

    # *Association not used*
    # Type M:0..n in CIM
    # Controls : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..n in CIM
    # Measurements : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM
    # Location : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.GL, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY, Profile.EQ, Profile.EQ_BD, Profile.SSH, Profile.GL,  }
