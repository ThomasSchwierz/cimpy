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
class ExcIEEEAC3A(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type AC3A model. The model represents the field-controlled alternator-
      rectifier excitation systems designated Type AC3A. These excitation systems include an alternator main exciter
      with non-controlled rectifiers. The exciter employs self-excitation, and the voltage regulator power is
      derived from the exciter output voltage.  Therefore, this system has an additional nonlinearity, simulated by
      the use of a multiplier whose inputs are the voltage regulator command signal, , and the exciter output
      voltage, , times .  This model is applicable to excitation systems employing static voltage regulators.
      Reference: IEEE Standard 421.5-2005 Section 6.3.

    tb: Voltage regulator time constant (T).  Typical Value = 0.
    tc: Voltage regulator time constant (T).  Typical Value = 0.
    ka: Voltage regulator gain (K).  Typical Value = 45.62.
    ta: Voltage regulator time constant (T).  Typical Value = 0.013.
    vamax: Maximum voltage regulator output (V).  Typical Value = 1.
    vamin: Minimum voltage regulator output (V).  Typical Value = -0.95.
    te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 1.17.
    vemin: Minimum exciter voltage output (V).  Typical Value = 0.1.
    kr: Constant associated with regulator and alternator field power supply (K).  Typical Value = 3.77.
    kf: Excitation control system stabilizer gains (K).  Typical Value = 0.143.
    tf: Excitation control system stabilizer time constant (T).  Typical Value = 1.
    kn: Excitation control system stabilizer gain (K).  Typical Value = 0.05.
    efdn: Value of at which feedback gain changes (E).  Typical Value = 2.36.
    kc: Rectifier loading factor proportional to commutating reactance (K).  Typical Value = 0.104.
    kd: Demagnetizing factor, a function of exciter alternator reactances (K).  Typical Value = 0.499.
    ke: Exciter constant related to self-excited field (K).  Typical Value = 1.
    vfemax: Exciter field current limit reference (V).  Typical Value = 16.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V) equals
      V(V).  Typical Value = 6.24.
    seve1: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance
      (S[V]).  Typical Value = 1.143.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V).  Typical
      Value = 4.68.
    seve2: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance
      (S[V]).  Typical Value = 0.1.
    """

    tb : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ka : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

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

    vfemax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

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
