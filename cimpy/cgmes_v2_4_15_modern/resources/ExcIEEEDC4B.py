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
class ExcIEEEDC4B(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type DC4B model. These excitation systems utilize a field-controlled dc
      commutator exciter with a continuously acting voltage regulator having supplies obtained from the generator or
      auxiliary bus.  Reference: IEEE Standard 421.5-2005 Section 5.4.

    ka: Voltage regulator gain (K).  Typical Value = 1.
    ta: Voltage regulator time constant (T).  Typical Value = 0.2.
    kp: Regulator proportional gain (K).  Typical Value = 20.
    ki: Regulator integral gain (K).  Typical Value = 20.
    kd: Regulator derivative gain (K).  Typical Value = 20.
    td: Regulator derivative filter time constant(T).  Typical Value = 0.01.
    vrmax: Maximum voltage regulator output (V).  Typical Value = 2.7.
    vrmin: Minimum voltage regulator output (V).  Typical Value = -0.9.
    ke: Exciter constant related to self-excited field (K).  Typical Value = 1.
    te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 0.8.
    kf: Excitation control system stabilizer gain (K).  Typical Value = 0.
    tf: Excitation control system stabilizer time constant (T).  Typical Value = 1.
    efd1: Exciter voltage at which exciter saturation is defined (E).  Typical Value = 1.75.
    seefd1: Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.08.
    efd2: Exciter voltage at which exciter saturation is defined (E).  Typical Value = 2.33.
    seefd2: Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.27.
    vemin: Minimum exciter voltage output(V).  Typical Value = 0.
    oelin: OEL input (OELin). true = LV gate false = subtract from error signal. Typical Value = true.
    uelin: UEL input (UELin). true = HV gate false = add to error signal. Typical Value = true.
    """

    ka : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ki : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kd : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    td : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ke : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    te : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kf : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tf : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efd1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    seefd1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efd2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    seefd2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vemin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    oelin : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    uelin : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
