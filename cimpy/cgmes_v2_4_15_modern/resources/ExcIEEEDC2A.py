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
class ExcIEEEDC2A(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type DC2A model. This model represents represent field-controlled dc
      commutator exciters with continuously acting voltage regulators having supplies obtained from the generator or
      auxiliary bus.  It differs from the Type DC1A model only in the voltage regulator output limits, which are now
      proportional to terminal voltage . It is representative of solid-state replacements for various forms of older
      mechanical and rotating amplifier regulating equipment connected to dc commutator exciters.  Reference: IEEE
      Standard 421.5-2005 Section 5.2.

    efd1: Exciter voltage at which exciter saturation is defined (E).  Typical Value = 3.05.
    efd2: Exciter voltage at which exciter saturation is defined (E).  Typical Value = 2.29.
    exclim: (exclim).  IEEE standard is ambiguous about lower limit on exciter output. Typical Value = - 999  which
      means that there is no limit applied.
    ka: Voltage regulator gain (K).  Typical Value = 300.
    ke: Exciter constant related to self-excited field (K).  Typical Value = 1.
    kf: Excitation control system stabilizer gain (K).  Typical Value = 0.1.
    seefd1: Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.279.
    seefd2: Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.117.
    ta: Voltage regulator time constant (T).  Typical Value = 0.01.
    tb: Voltage regulator time constant (T).  Typical Value = 0.
    tc: Voltage regulator time constant (T).  Typical Value = 0.
    te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 1.33.
    tf: Excitation control system stabilizer time constant (T).  Typical Value = 0.675.
    uelin: UEL input (uelin). true = input is connected to the HV gate false = input connects to the error signal.
      Typical Value = true.
    vrmax: Maximum voltage regulator output (V).  Typical Value = 4.95.
    vrmin: Minimum voltage regulator output (V).  Typical Value = -4.9.
    """

    efd1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efd2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    exclim : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ka : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ke : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kf : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    seefd1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    seefd2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tb : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    te : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tf : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    uelin : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
