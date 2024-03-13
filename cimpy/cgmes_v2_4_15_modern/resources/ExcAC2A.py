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
class ExcAC2A(ExcitationSystemDynamics):
    """
    Modified IEEE AC2A alternator-supplied rectifier excitation system with different field current limit.

    tb: Voltage regulator time constant (Tb).  Typical Value = 0.
    tc: Voltage regulator time constant (T).  Typical Value = 0.
    ka: Voltage regulator gain (Ka).  Typical Value = 400.
    ta: Voltage regulator time constant (Ta).  Typical Value = 0.02.
    vamax: Maximum voltage regulator output (V).  Typical Value = 8.
    vamin: Minimum voltage regulator output (V).  Typical Value = -8.
    kb: Second stage regulator gain (Kb) (>0).  Exciter field current controller gain.  Typical Value = 25.
    kb1: Second stage regulator gain (Kb1). It is exciter field current controller gain used as alternative to Kb to
      represent a variant of the ExcAC2A model.  Typical Value = 25.
    vrmax: Maximum voltage regulator outputs (Vrmax).  Typical Value = 105.
    vrmin: Minimum voltage regulator outputs (Vrmin).  Typical Value = -95.
    te: Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 0.6.
    vfemax: Exciter field current limit reference (Vfemax).  Typical Value = 4.4.
    kh: Exciter field current feedback gain (Kh).  Typical Value = 1.
    kf: Excitation control system stabilizer gains (Kf).  Typical Value = 0.03.
    kl: Exciter field current limiter gain (Kl).  Typical Value = 10.
    vlr: Maximum exciter field current (Vlr).  Typical Value = 4.4.
    kl1: Coefficient to allow different usage of the model (Kl1).  Typical Value = 1.
    ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0.
    tf: Excitation control system stabilizer time constant (Tf).  Typical Value = 1.
    kc: Rectifier loading factor proportional to commutating reactance (Kc).  Typical Value = 0.28.
    kd: Demagnetizing factor, a function of exciter alternator reactances (Kd).  Typical Value = 0.35.
    ke: Exciter constant related to self-excited field (Ke).  Typical Value = 1.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve).  Typical
      Value = 4.4.
    seve1: Exciter saturation function value at the corresponding exciter voltage, Ve, back of commutating reactance
      (Se[Ve]).  Typical Value = 0.037.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve).  Typical
      Value = 3.3.
    seve2: Exciter saturation function value at the corresponding exciter voltage, Ve, back of commutating reactance
      (Se[Ve]).  Typical Value = 0.012.
    hvgate: Indicates if HV gate is active (HVgate). true = gate is used false = gate is not used. Typical Value = true.
    lvgate: Indicates if LV gate is active (LVgate). true = gate is used false = gate is not used. Typical Value = true.
    """

    tb : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ka : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vamax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vamin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kb : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kb1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    te : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vfemax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kh : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kf : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kl : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vlr : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kl1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ks : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tf : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kd : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ke : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ve1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    seve1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ve2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    seve2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    hvgate : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    lvgate : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
