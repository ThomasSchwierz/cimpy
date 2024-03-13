"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .Connector import Connector

@dataclass
class BusbarSection(Connector):
    """
    A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment
      within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are
      connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled
      with exactly one logical terminal.

    ipMax: Maximum allowable peak short-circuit current of busbar (Ipmax in the IEC 60909-0).  Mechanical limit of the
      busbar in the substation itself. Used for short circuit data exchange according to IEC 60909
    """

    ipMax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
