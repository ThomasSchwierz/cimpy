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
class SubGeographicalRegion(IdentifiedObject):
    """
    A subset of a geographical region of a power system network model.

    DCLines: 
    Region: The geographical region to which this sub-geographical region is within.
    Lines: The lines within the sub-geographical region.
    Substations: The substations in this sub-geographical region.
    """

    # *Association not used*
    # Type M:0..n in CIM
    # DCLines : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    Region : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, Profile.EQ_BD, ]}) 

    # *Association not used*
    # Type M:0..n in CIM
    # Lines : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, Profile.EQ_BD, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..n in CIM
    # Substations : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ, Profile.EQ_BD,  }
