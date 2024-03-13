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
class ExcIEEEAC7B(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type AC7B model. The model represents excitation systems which consist of
      an ac alternator with either stationary or rotating rectifiers to produce the dc field requirements. It is an
      upgrade to earlier ac excitation systems, which replace only the controls but retain the ac alternator and
      diode rectifier bridge.  Reference: IEEE Standard 421.5-2005 Section 6.7.  In the IEEE Standard 421.5 - 2005,
      the [1 / sT] block is shown as [1 / (1 + sT)], which is incorrect.

    kpr: Voltage regulator proportional gain (K).  Typical Value = 4.24.
    kir: Voltage regulator integral gain (K).  Typical Value = 4.24.
    kdr: Voltage regulator derivative gain (K).  Typical Value = 0.
    tdr: Lag time constant (T).  Typical Value = 0.
    vrmax: Maximum voltage regulator output (V).  Typical Value = 5.79.
    vrmin: Minimum voltage regulator output (V).  Typical Value = -5.79.
    kpa: Voltage regulator proportional gain (K).  Typical Value = 65.36.
    kia: Voltage regulator integral gain (K).  Typical Value = 59.69.
    vamax: Maximum voltage regulator output (V).  Typical Value = 1.
    vamin: Minimum voltage regulator output (V).  Typical Value = -0.95.
    kp: Potential circuit gain coefficient (K).  Typical Value = 4.96.
    kl: Exciter field voltage lower limit parameter (K).  Typical Value = 10.
    te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 1.1.
    vfemax: Exciter field current limit reference (V).  Typical Value = 6.9.
    vemin: Minimum exciter voltage output (V).  Typical Value = 0.
    ke: Exciter constant related to self-excited field (K).  Typical Value = 1.
    kc: Rectifier loading factor proportional to commutating reactance (K). Typical Value = 0.18.
    kd: Demagnetizing factor, a function of exciter alternator reactances (K).  Typical Value = 0.02.
    kf1: Excitation control system stabilizer gain (K).  Typical Value = 0.212.
    kf2: Excitation control system stabilizer gain (K).  Typical Value = 0.
    kf3: Excitation control system stabilizer gain (K).  Typical Value = 0.
    tf: Excitation control system stabilizer time constant (T).  Typical Value = 1.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V) equals V
      (V).  Typical Value = 6.3.
    seve1: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance
      (S[V]).  Typical Value = 0.44.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V).  Typical
      Value = 3.02.
    seve2: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance
      (S[V]).  Typical Value = 0.075.
    """

    kpr : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kir : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kdr : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tdr : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kpa : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kia : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vamax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vamin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kl : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    te : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vfemax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vemin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ke : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kd : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kf1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kf2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kf3 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tf : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

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
