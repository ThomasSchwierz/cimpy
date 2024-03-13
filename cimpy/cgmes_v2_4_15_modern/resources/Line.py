"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .EquipmentContainer import EquipmentContainer

@dataclass
class Line(EquipmentContainer):
    """
    Contains equipment beyond a substation belonging to a power transmission line.

    Region: The sub-geographical region of the line.
    """

    Region : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, Profile.EQ_BD, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ, Profile.EQ_BD,  }
