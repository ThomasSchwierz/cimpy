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
class PssWECC(PowerSystemStabilizerDynamics):
    """
    Dual input Power System Stabilizer, based on IEEE type 2, with modified output limiter defined by WECC (Western
      Electricity Coordinating Council, USA).

    inputSignal1Type: Type of input signal #1.
    inputSignal2Type: Type of input signal #2.
    k1: Input signal 1 gain  (K).
    t1: Input signal 1 transducer time constant (T).
    k2: Input signal 2 gain (K).
    t2: Input signal 2 transducer time constant (T).
    t3: Stabilizer washout time constant (T).
    t4: Stabilizer washout time lag constant (T) (>0).
    t5: Lead time constant (T).
    t6: Lag time constant (T).
    t7: Lead time constant (T).
    t8: Lag time constant (T).
    t10: Lag time constant (T).
    t9: Lead time constant (T).
    vsmax: Maximum output signal (Vsmax).
    vsmin: Minimum output signal (Vsmin).
    vcu: Maximum value for voltage compensator output (V).
    vcl: Minimum value for voltage compensator output (V).
    """

    inputSignal1Type : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    inputSignal2Type : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t4 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t5 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t6 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t7 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t8 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t10 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t9 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vsmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vsmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vcu : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vcl : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
