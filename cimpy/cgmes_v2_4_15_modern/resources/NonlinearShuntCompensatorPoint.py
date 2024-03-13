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
class NonlinearShuntCompensatorPoint(Base):
    """
    A non linear shunt compensator bank or section admittance value.

    NonlinearShuntCompensator: Non-linear shunt compensator owning this point.
    b: Positive sequence shunt (charging) susceptance per section
    b0: Zero sequence shunt (charging) susceptance per section
    g: Positive sequence shunt (charging) conductance per section
    g0: Zero sequence shunt (charging) conductance per section
    sectionNumber: The number of the section.
    """

    NonlinearShuntCompensator : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    b : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    b0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    g : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    g0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    sectionNumber : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
