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
class ExcAC3A(ExcitationSystemDynamics):
    """
    Modified IEEE AC3A alternator-supplied rectifier excitation system with different field current limit.

    tb: Voltage regulator time constant (Tb).  Typical Value = 0.
    tc: Voltage regulator time constant (T).  Typical Value = 0.
    ka: Voltage regulator gain (Ka).  Typical Value = 45.62.
    ta: Voltage regulator time constant (Ta).  Typical Value = 0.013.
    vamax: Maximum voltage regulator output (V).  Typical Value = 1.
    vamin: Minimum voltage regulator output (V).  Typical Value = -0.95.
    te: Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 1.17.
    vemin: Minimum exciter voltage output (Vemin).  Typical Value = 0.1.
    kr: Constant associated with regulator and alternator field power supply (Kr).  Typical Value =3.77.
    kf: Excitation control system stabilizer gains (Kf).  Typical Value = 0.143.
    tf: Excitation control system stabilizer time constant (Tf).  Typical Value = 1.
    kn: Excitation control system stabilizer gain (Kn).  Typical Value =0.05.
    efdn: Value of at which feedback gain changes (Efdn).  Typical Value = 2.36.
    kc: Rectifier loading factor proportional to commutating reactance (Kc).  Typical Value = 0.104.
    kd: Demagnetizing factor, a function of exciter alternator reactances (Kd).  Typical Value = 0.499.
    ke: Exciter constant related to self-excited field (Ke).  Typical Value = 1.
    klv: Gain used in the minimum field voltage limiter loop (Klv).  Typical Value = 0.194.
    kf1: Coefficient to allow different usage of the model (Kf1).  Typical Value = 1.
    kf2: Coefficient to allow different usage of the model (Kf2).  Typical Value = 0.
    ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0.
    vfemax: Exciter field current limit reference (Vfemax).  Typical Value = 16.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve1) equals
      Vemax (Ve1).  Typical Value = 6.24.
    seve1: Exciter saturation function value at the corresponding exciter voltage, Ve, back of commutating reactance
      (Se[Ve]).  Typical Value = 1.143.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve).  Typical
      Value = 4.68.
    seve2: Exciter saturation function value at the corresponding exciter voltage, Ve, back of commutating reactance
      (Se[Ve]).  Typical Value = 0.1.
    vlv: Field voltage used in the minimum field voltage limiter loop (Vlv).  Typical Value = 0.79.
    """

    tb : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ka : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vamax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vamin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    te : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vemin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kr : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kf : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tf : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kn : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efdn : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kd : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ke : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    klv : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kf1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kf2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ks : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vfemax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ve1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    seve1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ve2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    seve2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vlv : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
