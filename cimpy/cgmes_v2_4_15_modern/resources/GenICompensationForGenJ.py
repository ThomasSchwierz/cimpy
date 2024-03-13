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
class GenICompensationForGenJ(IdentifiedObject):
    """
    This class provides the resistive and reactive components of compensation for the generator associated with the IEEE
      Type 2 voltage compensator for current flow out of one of the other generators in the interconnection.

    SynchronousMachineDynamics: Standard synchronous machine out of which current flow is being compensated for.
    VcompIEEEType2: The standard IEEE Type 2 voltage compensator of this compensation.
    rcij: 
    xcij: 
    """

    SynchronousMachineDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    VcompIEEEType2 : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rcij : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    xcij : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
