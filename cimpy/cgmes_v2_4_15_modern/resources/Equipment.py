"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .PowerSystemResource import PowerSystemResource

@dataclass
class Equipment(PowerSystemResource):
    """
    The parts of a power system that are physical devices, electronic or mechanical.

    aggregate: The single instance of equipment represents multiple pieces of equipment that have been modeled together
      as an aggregate.  Examples would be power transformers or synchronous machines operating in
      parallel modeled as a single aggregate power transformer or aggregate synchronous machine.  This is
      not to be used to indicate equipment that is part of a group of interdependent equipment produced
      by a network production program.
    EquipmentContainer: Container of this equipment.
    OperationalLimitSet: The operational limit sets associated with this equipment.
    """

    aggregate : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    EquipmentContainer : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, Profile.EQ_BD, ]}) 

    # *Association not used*
    # Type M:0..n in CIM
    # OperationalLimitSet : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY, Profile.EQ, Profile.EQ_BD, Profile.SSH,  }
