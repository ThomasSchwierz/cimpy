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
class BaseVoltage(IdentifiedObject):
    """
    Defines a system base voltage which is referenced.

    nominalVoltage: The power system resource`s base voltage.
    ConductingEquipment: Base voltage of this conducting equipment.  Use only when there is no voltage level container
      used and only one base voltage applies.  For example, not used for transformers.
    VoltageLevel: The voltage levels having this base voltage.
    TransformerEnds: Transformer ends at the base voltage.  This is essential for PU calculation.
    TopologicalNode: The topological nodes at the base voltage.
    """

    nominalVoltage : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, Profile.EQ_BD, ]}) 

    # *Association not used*
    # Type M:0..n in CIM
    # ConductingEquipment : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..n in CIM
    # VoltageLevel : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..n in CIM
    # TransformerEnds : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..n in CIM
    # TopologicalNode : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.TP_BD, Profile.TP, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ, Profile.EQ_BD, Profile.TP_BD, Profile.TP,  }
