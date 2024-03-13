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
class BusNameMarker(IdentifiedObject):
    """
    Used to apply user standard names to topology buses. Typically used for "bus/branch" case generation. Associated
      with one or more terminals that are normally connected with the bus name.    The associated terminals are
      normally connected by non-retained switches. For a ring bus station configuration, all busbar terminals in the
      ring are typically associated.   For a breaker and a half scheme, both busbars would normally be associated.
      For a ring bus, all busbars would normally be associated.  For a "straight" busbar configuration, normally
      only the main terminal at the busbar would be associated.

    priority: Priority of bus name marker for use as topology bus name.  Use 0 for don t care.  Use 1 for highest
      priority.  Use 2 as priority is less than 1 and so on.
    ReportingGroup: The bus name markers that belong to this reporting group.
    Terminal: The terminals associated with this bus name marker.
    """

    priority : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    ReportingGroup : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    # *Association not used*
    # Type M:1..n in CIM
    # Terminal : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
