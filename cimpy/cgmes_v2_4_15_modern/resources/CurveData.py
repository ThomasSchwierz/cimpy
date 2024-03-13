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
class CurveData(Base):
    """
    Multi-purpose data points for defining a curve.  The use of this generic class is discouraged if a more specific
      class  can be used to specify the x and y axis values along with their specific data types.

    Curve: The point data values that define this curve.
    xvalue: The data value of the X-axis variable,  depending on the X-axis units.
    y1value: The data value of the  first Y-axis variable, depending on the Y-axis units.
    y2value: The data value of the second Y-axis variable (if present), depending on the Y-axis units.
    """

    Curve : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    xvalue : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    y1value : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    y2value : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
