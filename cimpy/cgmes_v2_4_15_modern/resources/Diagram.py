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
class Diagram(IdentifiedObject):
    """
    The diagram being exchanged.  The coordinate system is a standard Cartesian coordinate system and the orientation
      attribute defines the orientation.

    DiagramStyle: A Diagram may have a DiagramStyle.
    orientation: Coordinate system orientation of the diagram.
    x1InitialView: X coordinate of the first corner of the initial view.
    x2InitialView: X coordinate of the second corner of the initial view.
    y1InitialView: Y coordinate of the first corner of the initial view.
    y2InitialView: Y coordinate of the second corner of the initial view.
    DiagramElements: A diagram is made up of multiple diagram objects.
    """

    DiagramStyle : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DL, ]}) 

    orientation : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DL, ]}) 

    x1InitialView : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DL, ]}) 

    x2InitialView : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DL, ]}) 

    y1InitialView : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DL, ]}) 

    y2InitialView : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DL, ]}) 

    # *Association not used*
    # Type M:0..n in CIM
    # DiagramElements : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DL, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DL,  }
