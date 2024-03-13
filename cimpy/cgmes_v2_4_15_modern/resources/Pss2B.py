"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics

@dataclass
class Pss2B(PowerSystemStabilizerDynamics):
    """
    Modified IEEE PSS2B Model.  Extra lead/lag (or rate) block added at end (up to 4 lead/lags total).

    inputSignal1Type: Type of input signal #1.  Typical Value = rotorSpeed.
    inputSignal2Type: Type of input signal #2.  Typical Value = generatorElectricalPower.
    vsi1max: Input signal #1 max limit (Vsi1max).  Typical Value = 2.
    vsi1min: Input signal #1 min limit (Vsi1min).  Typical Value = -2.
    tw1: First washout on signal #1 (Tw1).  Typical Value = 2.
    tw2: Second washout on signal #1 (Tw2).  Typical Value = 2.
    vsi2max: Input signal #2 max limit (Vsi2max).  Typical Value = 2.
    vsi2min: Input signal #2 min limit (Vsi2min).  Typical Value = -2.
    tw3: First washout on signal #2 (Tw3).  Typical Value = 2.
    tw4: Second washout on signal #2 (Tw4).  Typical Value = 0.
    t1: Lead/lag time constant (T1).  Typical Value = 0.12.
    t2: Lead/lag time constant (T2).  Typical Value = 0.02.
    t3: Lead/lag time constant (T3).  Typical Value = 0.3.
    t4: Lead/lag time constant (T4).  Typical Value = 0.02.
    t6: Time constant on signal #1 (T6).  Typical Value = 0.
    t7: Time constant on signal #2 (T7).  Typical Value = 2.
    t8: Lead of ramp tracking filter (T8).  Typical Value = 0.2.
    t9: Lag of ramp tracking filter (T9).  Typical Value = 0.1.
    t10: Lead/lag time constant (T10).  Typical Value = 0.
    t11: Lead/lag time constant (T11).  Typical Value = 0.
    ks1: Stabilizer gain (Ks1).  Typical Value = 12.
    ks2: Gain on signal #2 (Ks2).  Typical Value = 0.2.
    ks3: Gain on signal #2 input before ramp-tracking filter (Ks3).  Typical Value = 1.
    ks4: Gain on signal #2 input after ramp-tracking filter (Ks4).  Typical Value = 1.
    n: Order of ramp tracking filter (N).  Typical Value = 1.
    m: Denominator order of ramp tracking filter (M).  Typical Value = 5.
    vstmax: Stabilizer output max limit (Vstmax).  Typical Value = 0.1.
    vstmin: Stabilizer output min limit (Vstmin).  Typical Value = -0.1.
    a: Numerator constant (a).  Typical Value = 1.
    ta: Lead constant (Ta).  Typical Value = 0.
    tb: Lag time constant (Tb).  Typical Value = 0.
    """

    inputSignal1Type : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    inputSignal2Type : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vsi1max : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vsi1min : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tw1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tw2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vsi2max : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vsi2min : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tw3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tw4 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t4 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t6 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t7 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t8 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t9 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t10 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t11 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ks1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ks2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ks3 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ks4 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    n : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    m : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vstmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vstmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    a : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tb : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
