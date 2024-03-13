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
class SvInjection(Base):
    """
    The SvInjection is reporting the calculated bus injection minus the sum of the terminal flows. The terminal flow is
      positive out from the bus (load sign convention) and bus injection has positive flow into the bus. SvInjection
      may have the remainder after state estimation or slack after power flow calculation.

    pInjection: The active power injected into the bus in addition to injections from equipment terminals.  Positive
      sign means injection into the TopologicalNode (bus).
    qInjection: The reactive power injected into the bus in addition to injections from equipment terminals. Positive
      sign means injection into the TopologicalNode (bus).
    TopologicalNode: The injection flows state variables associated with the topological node.
    """

    pInjection : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SV, ]}) 

    qInjection : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SV, ]}) 

    TopologicalNode : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.SV, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.SV,  }
