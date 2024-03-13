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
class ExcIEEEAC6A(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type AC6A model. The model represents field-controlled alternator-rectifier
      excitation systems with system-supplied electronic voltage regulators.  The maximum output of the regulator, ,
      is a function of terminal voltage, . The field current limiter included in the original model AC6A remains in
      the 2005 update.  Reference: IEEE Standard 421.5-2005 Section 6.6.

    ka: Voltage regulator gain (K).  Typical Value = 536.
    ta: Voltage regulator time constant (T).  Typical Value = 0.086.
    tk: Voltage regulator time constant (T).  Typical Value = 0.18.
    tb: Voltage regulator time constant (T).  Typical Value = 9.
    tc: Voltage regulator time constant (T).  Typical Value = 3.
    vamax: Maximum voltage regulator output (V).  Typical Value = 75.
    vamin: Minimum voltage regulator output (V).  Typical Value = -75.
    vrmax: Maximum voltage regulator output (V).  Typical Value = 44.
    vrmin: Minimum voltage regulator output (V).  Typical Value = -36.
    te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 1.
    kh: Exciter field current limiter gain (K).  Typical Value = 92.
    tj: Exciter field current limiter time constant (T).  Typical Value = 0.02.
    th: Exciter field current limiter time constant (T).  Typical Value = 0.08.
    vfelim: Exciter field current limit reference (V).  Typical Value = 19.
    vhmax: Maximum field current limiter signal reference (V).  Typical Value = 75.
    kc: Rectifier loading factor proportional to commutating reactance (K). Typical Value = 0.173.
    kd: Demagnetizing factor, a function of exciter alternator reactances (K).  Typical Value = 1.91.
    ke: Exciter constant related to self-excited field (K).  Typical Value = 1.6.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V) equals
      V(V).  Typical Value = 7.4.
    seve1: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance
      (S[V]).  Typical Value = 0.214.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V).  Typical
      Value = 5.55.
    seve2: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance
      (S[V]).  Typical Value = 0.044.
    """

    ka : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tk : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tb : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vamax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vamin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    te : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kh : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tj : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    th : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vfelim : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vhmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

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
