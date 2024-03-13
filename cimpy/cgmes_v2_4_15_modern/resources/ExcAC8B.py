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
class ExcAC8B(ExcitationSystemDynamics):
    """
    Modified IEEE AC8B alternator-supplied rectifier excitation system with speed input and input limiter.

    inlim: Input limiter indicator. true = input limiter Vimax and Vimin is considered false = input limiter Vimax and
      Vimin is not considered. Typical Value = true.
    ka: Voltage regulator gain (Ka).  Typical Value = 1.
    kc: Rectifier loading factor proportional to commutating reactance (Kc). Typical Value = 0.55.
    kd: Demagnetizing factor, a function of exciter alternator reactances (Kd).  Typical Value = 1.1.
    kdr: Voltage regulator derivative gain (Kdr).  Typical Value = 10.
    ke: Exciter constant related to self-excited field (Ke).  Typical Value = 1.
    kir: Voltage regulator integral gain (Kir).  Typical Value = 5.
    kpr: Voltage regulator proportional gain (Kpr).  Typical Value = 80.
    ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0.
    pidlim: PID limiter indicator. true = input limiter Vpidmax and Vpidmin is considered false = input limiter Vpidmax
      and Vpidmin is not considered. Typical Value = true.
    seve1: Exciter saturation function value at the corresponding exciter voltage, Ve, back of commutating reactance
      (Se[Ve1]).  Typical Value = 0.3.
    seve2: Exciter saturation function value at the corresponding exciter voltage, Ve, back of commutating reactance
      (Se[Ve2]).  Typical Value = 3.
    ta: Voltage regulator time constant (Ta).  Typical Value = 0.
    tdr: Lag time constant (Tdr).  Typical Value = 0.1.
    te: Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 1.2.
    telim: Selector for the limiter on the block [1/sTe].  See diagram for meaning of true and false. Typical Value =
      false.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve) equals V
      (Ve1).  Typical Value = 6.5.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (Ve).  Typical
      Value = 9.
    vemin: Minimum exciter voltage output (Vemin).  Typical Value = 0.
    vfemax: Exciter field current limit reference (Vfemax).  Typical Value = 6.
    vimax: Input signal maximum (Vimax).  Typical Value = 35.
    vimin: Input signal minimum (Vimin).  Typical Value = -10.
    vpidmax: PID maximum controller output (Vpidmax).  Typical Value = 35.
    vpidmin: PID minimum controller output (Vpidmin).  Typical Value = -10.
    vrmax: Maximum voltage regulator output (Vrmax). Typical Value = 35.
    vrmin: Minimum voltage regulator output (Vrmin).  Typical Value = 0.
    vtmult: Multiply by generator`s terminal voltage indicator. true =the limits Vrmax and Vrmin are multiplied by the
      generator`s terminal voltage to represent a thyristor power stage fed from the generator terminals
      false = limits are not multiplied by generator`s terminal voltage.  Typical Value = false.
    """

    inlim : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ka : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kd : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kdr : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ke : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kir : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kpr : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ks : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pidlim : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    seve1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    seve2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tdr : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    te : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    telim : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ve1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ve2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vemin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vfemax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vimax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vimin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vpidmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vpidmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vtmult : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
