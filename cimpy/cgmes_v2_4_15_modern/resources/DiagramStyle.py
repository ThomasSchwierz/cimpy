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
class DiagramStyle(IdentifiedObject):
    """
    The diagram style refer to a style used by the originating system for a diagram.  A diagram style describes
      information such as schematic, geographic, bus-branch etc.

    Diagram: A DiagramStyle can be used by many Diagrams.
    """

    # *Association not used*
    # Type M:0..n in CIM
    # Diagram : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DL, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DL,  }
