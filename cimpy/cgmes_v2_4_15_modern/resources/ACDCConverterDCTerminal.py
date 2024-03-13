"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .DCBaseTerminal import DCBaseTerminal

@dataclass
class ACDCConverterDCTerminal(DCBaseTerminal):
    """
    A DC electrical connection point at the AC/DC converter. The AC/DC converter is electrically connected also to the
      AC side. The AC connection is inherited from the AC conducting equipment in the same way as any other AC
      equipment. The AC/DC converter DC terminal is separate from generic DC terminal to restrict the connection
      with the AC side to AC/DC converter and so that no other DC conducting equipment can be connected to the AC
      side.

    DCConductingEquipment: 
    polarity: Represents the normal network polarity condition.
    """

    DCConductingEquipment : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    polarity : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ, Profile.SSH, Profile.TP,  }
