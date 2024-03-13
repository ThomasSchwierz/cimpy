"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcIEEEAC2A(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type AC2A model. The model represents a high initial response field-
      controlled alternator-rectifier excitation system. The alternator main exciter is used with non-controlled
      rectifiers. The Type AC2A model is similar to that of Type AC1A except for the inclusion of exciter time
      constant compensation and exciter field current limiting elements.  Reference: IEEE Standard 421.5-2005
      Section 6.2.

    tb: Voltage regulator time constant (T).  Typical Value = 0.
    tc: Voltage regulator time constant (T).  Typical Value = 0.
    ka: Voltage regulator gain (K).  Typical Value = 400.
    ta: Voltage regulator time constant (T).  Typical Value = 0.02.
    vamax: Maximum voltage regulator output (V).  Typical Value = 8.
    vamin: Minimum voltage regulator output (V).  Typical Value = -8.
    kb: Second stage regulator gain (K).  Typical Value = 25.
    vrmax: Maximum voltage regulator outputs (V).  Typical Value = 105.
    vrmin: Minimum voltage regulator outputs (V).  Typical Value = -95.
    te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 0.6.
    vfemax: Exciter field current limit reference (V).  Typical Value = 4.4.
    kh: Exciter field current feedback gain (K).  Typical Value = 1.
    kf: Excitation control system stabilizer gains (K).  Typical Value = 0.03.
    tf: Excitation control system stabilizer time constant (T).  Typical Value = 1.
    kc: Rectifier loading factor proportional to commutating reactance (K).  Typical Value = 0.28.
    kd: Demagnetizing factor, a function of exciter alternator reactances (K).  Typical Value = 0.35.
    ke: Exciter constant related to self-excited field (K).  Typical Value = 1.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V).  Typical
      Value = 4.4.
    seve1: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance
      (S[V]).  Typical Value = 0.037.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V).  Typical
      Value = 3.3.
    seve2: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance
      (S[V]).  Typical Value = 0.012.
    """

    tb : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ka : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vamax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vamin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kb : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    te : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vfemax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kh : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kf : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tf : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kd : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ke : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ve1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    seve1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ve2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    seve2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
