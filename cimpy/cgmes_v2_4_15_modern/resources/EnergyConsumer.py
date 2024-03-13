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
class EnergyConsumer(ConductingEquipment):
    """
    Generic user of energy - a  point of consumption on the power system model.

    LoadDynamics: Load dynamics model used to describe dynamic behavior of this energy consumer.
    pfixed: Active power of the load that is a fixed quantity. Load sign convention is used, i.e. positive sign means
      flow out from a node.
    pfixedPct: Fixed active power as per cent of load group fixed active power. Load sign convention is used, i.e.
      positive sign means flow out from a node.
    qfixed: Reactive power of the load that is a fixed quantity. Load sign convention is used, i.e. positive sign means
      flow out from a node.
    qfixedPct: Fixed reactive power as per cent of load group fixed reactive power. Load sign convention is used, i.e.
      positive sign means flow out from a node.
    LoadResponse: The load response characteristic of this load.  If missing, this load is assumed to be constant power.
    p: Active power of the load. Load sign convention is used, i.e. positive sign means flow out from a node. For
      voltage dependent loads the value is at rated voltage. Starting value for a steady state solution.
    q: Reactive power of the load. Load sign convention is used, i.e. positive sign means flow out from a node. For
      voltage dependent loads the value is at rated voltage. Starting value for a steady state solution.
    """

    LoadDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pfixed : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    pfixedPct : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    qfixed : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    qfixedPct : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    LoadResponse : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    p : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    q : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY, Profile.EQ, Profile.SSH,  }
