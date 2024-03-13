"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcAVR5(ExcitationSystemDynamics):
    """
    Manual excitation control with field circuit resistance. This model can be used as a very simple representation of
      manual voltage control.

    ka: Gain (Ka).
    ta: Time constant (Ta).
    rex: Effective Output Resistance (Rex). Rex represents the effective output resistance seen by the excitation
      system.
    """

    ka : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rex : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
