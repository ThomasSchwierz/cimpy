"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .EquipmentContainer import EquipmentContainer

@dataclass
class VoltageLevel(EquipmentContainer):
    """
    A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of
      breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all
      these.

    BaseVoltage: The base voltage used for all equipment within the voltage level.
    Bays: The bays within this voltage level.
    Substation: The substation of the voltage level.
    highVoltageLimit: The bus bar`s high voltage limit
    lowVoltageLimit: The bus bar`s low voltage limit
    """

    BaseVoltage : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    # *Association not used*
    # Type M:0..n in CIM
    # Bays : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    Substation : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    highVoltageLimit : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    lowVoltageLimit : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
