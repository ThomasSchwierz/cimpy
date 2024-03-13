"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics

@dataclass
class DiscExcContIEEEDEC2A(DiscontinuousExcitationControlDynamics):
    """
    The class represents IEEE Type DEC2A model for the discontinuous excitation control. This system provides transient
      excitation boosting via an open-loop control as initiated by a trigger signal generated remotely.  Reference:
      IEEE Standard 421.5-2005 Section 12.3.

    vk: Discontinuous controller input reference ().
    td1: Discontinuous controller time constant ().
    td2: Discontinuous controller washout time constant ().
    vdmin: Limiter ().
    vdmax: Limiter ().
    """

    vk : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    td1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    td2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vdmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vdmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
