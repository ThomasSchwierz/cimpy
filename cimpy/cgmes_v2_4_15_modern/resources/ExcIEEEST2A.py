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
class ExcIEEEST2A(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type ST2A model. Some static systems utilize both current and voltage
      sources (generator terminal quantities) to comprise the power source.  The regulator controls the exciter
      output through controlled saturation of the power transformer components.  These compound-source rectifier
      excitation systems are designated Type ST2A and are represented by ExcIEEEST2A.  Reference: IEEE Standard
      421.5-2005 Section 7.2.

    ka: Voltage regulator gain (K).  Typical Value = 120.
    ta: Voltage regulator time constant (T).  Typical Value = 0.15.
    vrmax: Maximum voltage regulator outputs (V).  Typical Value = 1.
    vrmin: Minimum voltage regulator outputs (V).  Typical Value = 0.
    ke: Exciter constant related to self-excited field (K).  Typical Value = 1.
    te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 0.5.
    kf: Excitation control system stabilizer gains (K).  Typical Value = 0.05.
    tf: Excitation control system stabilizer time constant (T).  Typical Value = 1.
    kp: Potential circuit gain coefficient (K).  Typical Value = 4.88.
    ki: Potential circuit gain coefficient (K).  Typical Value = 8.
    kc: Rectifier loading factor proportional to commutating reactance (K). Typical Value = 1.82.
    efdmax: Maximum field voltage (E).  Typical Value = 99.
    uelin: UEL input (UELin). true = HV gate false = add to error signal. Typical Value = true.
    """

    ka : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ke : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    te : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kf : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tf : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ki : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efdmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    uelin : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
