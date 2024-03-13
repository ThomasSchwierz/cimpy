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
class EnergySource(ConductingEquipment):
    """
    A generic equivalent for an energy supplier on a transmission or distribution voltage level.

    WindTurbineType3or4Dynamics: Wind generator Type 3 or 4 dynamics model associated with this energy source.
    EnergySchedulingType: Energy Source of a particular Energy Scheduling Type
    nominalVoltage: Phase-to-phase nominal voltage.
    r: Positive sequence Thevenin resistance.
    r0: Zero sequence Thevenin resistance.
    rn: Negative sequence Thevenin resistance.
    voltageAngle: Phase angle of a-phase open circuit.
    voltageMagnitude: Phase-to-phase open circuit voltage magnitude.
    x: Positive sequence Thevenin reactance.
    x0: Zero sequence Thevenin reactance.
    xn: Negative sequence Thevenin reactance.
    activePower: High voltage source active injection. Load sign convention is used, i.e. positive sign means flow out
      from a node. Starting value for steady state solutions.
    reactivePower: High voltage source reactive injection. Load sign convention is used, i.e. positive sign means flow
      out from a node. Starting value for steady state solutions.
    """

    # *Association not used*
    # Type M:0..1 in CIM
    # WindTurbineType3or4Dynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    EnergySchedulingType : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, Profile.EQ_BD, ]}) 

    nominalVoltage : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    r : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    r0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    rn : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    voltageAngle : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    voltageMagnitude : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    x : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    x0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    xn : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    activePower : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    reactivePower : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY, Profile.EQ, Profile.EQ_BD, Profile.SSH,  }
