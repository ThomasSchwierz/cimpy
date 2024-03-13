"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .ShuntCompensator import ShuntCompensator

@dataclass
class LinearShuntCompensator(ShuntCompensator):
    """
    A linear shunt compensator has banks or sections with equal admittance values.

    b0PerSection: Zero sequence shunt (charging) susceptance per section
    bPerSection: Positive sequence shunt (charging) susceptance per section
    g0PerSection: Zero sequence shunt (charging) conductance per section
    gPerSection: Positive sequence shunt (charging) conductance per section
    """

    b0PerSection : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    bPerSection : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    g0PerSection : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    gPerSection : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ, Profile.SSH,  }
