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
class ACDCConverter(ConductingEquipment):
    """
    A unit with valves for three phases, together with unit control equipment, essential protective and switching
      devices, DC storage capacitors, phase reactors and auxiliaries, if any, used for conversion.

    baseS: Base apparent power of the converter pole.
    idleLoss: Active power loss in pole at no power transfer. Converter configuration data used in power flow.
    maxUdc: The maximum voltage on the DC side at which the converter should operate. Converter configuration data used
      in power flow.
    minUdc: Min allowed converter DC voltage. Converter configuration data used in power flow.
    numberOfValves: Number of valves in the converter. Used in loss calculations.
    ratedUdc: Rated converter DC voltage, also called UdN. Converter configuration data used in power flow.
    resistiveLoss: Converter configuration data used in power flow. Refer to poleLossP.
    switchingLoss: Switching losses, relative to the base apparent power `baseS`. Refer to poleLossP.
    valveU0: Valve threshold voltage. Forward voltage drop when the valve is conducting. Used in loss calculations, i.e.
      the switchLoss depend on numberOfValves * valveU0.
    DCTerminals: 
    PccTerminal: All converters` DC sides linked to this point of common coupling terminal.
    idc: Converter DC current, also called Id. Converter state variable, result from power flow.
    poleLossP: The active power loss at a DC Pole  = idleLoss + switchingLoss*|Idc| + resitiveLoss*Idc^2 For lossless
      operation Pdc=Pac For rectifier operation with losses Pdc=Pac-lossP For inverter operation with
      losses Pdc=Pac+lossP Converter state variable used in power flow.
    uc: Converter voltage, the voltage at the AC side of the bridge. Converter state variable, result from power flow.
    udc: Converter voltage at the DC side, also called Ud. Converter state variable, result from power flow.
    p: Active power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out
      from a node. Starting value for a steady state solution in the case a simplified power flow model is used.
    q: Reactive power at the point of common coupling. Load sign convention is used, i.e. positive sign means flow out
      from a node. Starting value for a steady state solution in the case a simplified power flow model is used.
    targetPpcc: Real power injection target in AC grid, at point of common coupling.
    targetUdc: Target value for DC voltage magnitude.
    """

    baseS : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    idleLoss : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    maxUdc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    minUdc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    numberOfValves : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    ratedUdc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    resistiveLoss : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    switchingLoss : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    valveU0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    # *Association not used*
    # Type M:0..n in CIM
    # DCTerminals : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    PccTerminal : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    idc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SV, ]}) 

    poleLossP : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SV, ]}) 

    uc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SV, ]}) 

    udc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SV, ]}) 

    p : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    q : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    targetPpcc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    targetUdc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ, Profile.SV, Profile.SSH,  }
