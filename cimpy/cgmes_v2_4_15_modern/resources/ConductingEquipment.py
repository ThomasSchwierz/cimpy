"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .Equipment import Equipment

@dataclass
class ConductingEquipment(Equipment):
    """
    The parts of the AC power system that are designed to carry current or that are conductively connected through
      terminals.

    Terminals: Conducting equipment have terminals that may be connected to other conducting equipment terminals via
      connectivity nodes or topological nodes.
    BaseVoltage: All conducting equipment with this base voltage.  Use only when there is no voltage level container
      used and only one base voltage applies.  For example, not used for transformers.
    SvStatus: The status state variable associated with this conducting equipment.
    """

    # *Association not used*
    # Type M:0..n in CIM
    # Terminals : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DY, Profile.EQ, Profile.EQ_BD, ]}) # noqa: E501

    BaseVoltage : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    # *Association not used*
    # Type M:0..1 in CIM
    # SvStatus : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.SV, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY, Profile.EQ, Profile.SV, Profile.EQ_BD, Profile.SSH,  }
