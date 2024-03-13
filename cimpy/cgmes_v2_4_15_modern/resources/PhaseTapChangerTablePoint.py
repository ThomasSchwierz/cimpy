"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .TapChangerTablePoint import TapChangerTablePoint

@dataclass
class PhaseTapChangerTablePoint(TapChangerTablePoint):
    """
    Describes each tap step in the phase tap changer tabular curve.

    PhaseTapChangerTable: The table of this point.
    angle: The angle difference in degrees.
    """

    PhaseTapChangerTable : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    angle : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
