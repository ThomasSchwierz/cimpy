"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .ACDCConverter import ACDCConverter

@dataclass
class VsConverter(ACDCConverter):
    """
    DC side of the voltage source converter (VSC).

    CapabilityCurve: All converters with this capability curve.
    maxModulationIndex: The max quotient between the AC converter voltage (Uc) and DC voltage (Ud). A factor typically
      less than 1. VSC configuration data used in power flow.
    maxValveCurrent: The maximum current through a valve. This current limit is the basis for calculating the capability
      diagram. VSC  configuration data.
    delta: Angle between uf and uc. Converter state variable used in power flow.
    uf: Filter bus voltage. Converter state variable, result from power flow.
    droop: Droop constant; pu value is obtained as D [kV^2 / MW] x Sb / Ubdc^2.
    droopCompensation: Compensation (resistance) constant. Used to compensate for voltage drop when controlling voltage
      at a distant bus.
    pPccControl: Kind of control of real power and/or DC voltage.
    qPccControl: 
    qShare: Reactive power sharing factor among parallel converters on Uac control.
    targetQpcc: Reactive power injection target in AC grid, at point of common coupling.
    targetUpcc: Voltage target in AC grid, at point of common coupling.
    """

    CapabilityCurve : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    maxModulationIndex : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    maxValveCurrent : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    delta : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SV, ]}) 

    uf : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SV, ]}) 

    droop : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    droopCompensation : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    pPccControl : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    qPccControl : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    qShare : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    targetQpcc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    targetUpcc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ, Profile.SV, Profile.SSH,  }
