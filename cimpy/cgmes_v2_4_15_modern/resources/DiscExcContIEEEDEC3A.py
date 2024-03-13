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
class DiscExcContIEEEDEC3A(DiscontinuousExcitationControlDynamics):
    """
    The class represents IEEE Type DEC3A model. In some systems, the stabilizer output is disconnected from the
      regulator immediately following a severe fault to prevent the stabilizer from competing with action of voltage
      regulator during the first swing.  Reference: IEEE Standard 421.5-2005 Section 12.4.

    vtmin: Terminal undervoltage comparison level ().
    tdr: Reset time delay ().
    """

    vtmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tdr : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
