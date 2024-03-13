"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .ConductingEquipment import ConductingEquipment

@dataclass
class Switch(ConductingEquipment):
    """
    A generic device designed to close, or open, or both, one or more electric circuits.  All switches are two terminal
      devices including grounding switches.

    normalOpen: The attribute is used in cases when no Measurement for the status value is present. If the Switch has a
      status measurement the Discrete.normalValue is expected to match with the Switch.normalOpen.
    ratedCurrent: The maximum continuous current carrying capacity in amps governed by the device material and
      construction.
    retained: Branch is retained in a bus branch model.  The flow through retained switches will normally be calculated
      in power flow.
    SwitchSchedules: A SwitchSchedule is associated with a Switch.
    open: The attribute tells if the switch is considered open when used as input to topology processing.
    """

    normalOpen : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    ratedCurrent : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    retained : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    # *Association not used*
    # Type M:0..n in CIM
    # SwitchSchedules : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    open : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ, Profile.SSH,  }
