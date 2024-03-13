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
class Pss2ST(PowerSystemStabilizerDynamics):
    """
    PTI Microprocessor-Based Stabilizer type 1.

    inputSignal1Type: Type of input signal #1.  Typical Value = rotorAngularFrequencyDeviation.
    inputSignal2Type: Type of input signal #2.  Typical Value = generatorElectricalPower.
    k1: Gain (K1).
    k2: Gain (K2).
    t1: Time constant (T1).
    t2: Time constant (T2).
    t3: Time constant (T3).
    t4: Time constant (T4).
    t5: Time constant (T5).
    t6: Time constant (T6).
    t7: Time constant (T7).
    t8: Time constant (T8).
    t9: Time constant (T9).
    t10: Time constant (T10).
    lsmax: Limiter (Lsmax).
    lsmin: Limiter (Lsmin).
    vcu: Cutoff limiter (Vcu).
    vcl: Cutoff limiter (Vcl).
    """

    inputSignal1Type : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    inputSignal2Type : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t4 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t5 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t6 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t7 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t8 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t9 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t10 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    lsmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    lsmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vcu : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vcl : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
