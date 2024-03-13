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
class DiagramObjectPoint(Base):
    """
    A point in a given space defined by 3 coordinates and associated to a diagram object.  The coordinates may be
      positive or negative as the origin does not have to be in the corner of a diagram.

    DiagramObject: The diagram object with which the points are associated.
    DiagramObjectGluePoint: A diagram object glue point is associated with 2 or more object points that are considered
      to be `glued` together.
    sequenceNumber: The sequence position of the point, used for defining the order of points for diagram objects acting
      as a polyline or polygon with more than one point.
    xPosition: The X coordinate of this point.
    yPosition: The Y coordinate of this point.
    zPosition: The Z coordinate of this point.
    """

    DiagramObject : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DL, ]}) 

    DiagramObjectGluePoint : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DL, ]}) 

    sequenceNumber : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DL, ]}) 

    xPosition : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DL, ]}) 

    yPosition : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DL, ]}) 

    zPosition : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DL, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DL,  }
