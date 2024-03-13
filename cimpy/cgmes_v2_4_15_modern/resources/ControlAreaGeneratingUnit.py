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
class ControlAreaGeneratingUnit(IdentifiedObject):
    """
    A control area generating unit. This class is needed so that alternate control area definitions may include the same
      generating unit.   Note only one instance within a control area should reference a specific generating unit.

    GeneratingUnit: The generating unit specified for this control area.  Note that a control area should include a
      GeneratingUnit only once.
    ControlArea: The parent control area for the generating unit specifications.
    """

    GeneratingUnit : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    ControlArea : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
