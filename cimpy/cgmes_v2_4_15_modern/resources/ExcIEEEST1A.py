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
class ExcIEEEST1A(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type ST1A model. This model represents systems in which excitation power is
      supplied through a transformer from the generator terminals (or the unit's auxiliary bus) and is regulated by
      a controlled rectifier.  The maximum exciter voltage available from such systems is directly related to the
      generator terminal voltage.  Reference: IEEE Standard 421.5-2005 Section 7.1.

    ilr: Exciter output current limit reference (I).  Typical Value = 0.
    ka: Voltage regulator gain (K).  Typical Value = 190.
    kc: Rectifier loading factor proportional to commutating reactance (K). Typical Value = 0.08.
    kf: Excitation control system stabilizer gains (K).  Typical Value = 0.
    klr: Exciter output current limiter gain (K).  Typical Value = 0.
    pssin: Selector of the Power System Stabilizer (PSS) input (PSSin). true = PSS input (Vs) added to error signal
      false = PSS input (Vs) added to voltage regulator output. Typical Value = true.
    ta: Voltage regulator time constant (T).  Typical Value = 0.
    tb: Voltage regulator time constant (T).  Typical Value = 10.
    tb1: Voltage regulator time constant (T).  Typical Value = 0.
    tc: Voltage regulator time constant (T).  Typical Value = 1.
    tc1: Voltage regulator time constant (T).  Typical Value = 0.
    tf: Excitation control system stabilizer time constant (T).  Typical Value = 1.
    uelin: Selector of the connection of the UEL input (UELin). Typical Value = ignoreUELsignal.
    vamax: Maximum voltage regulator output (V).  Typical Value = 14.5.
    vamin: Minimum voltage regulator output (V).  Typical Value = -14.5.
    vimax: Maximum voltage regulator input limit (V).  Typical Value = 999.
    vimin: Minimum voltage regulator input limit (V).  Typical Value = -999.
    vrmax: Maximum voltage regulator outputs (V).  Typical Value = 7.8.
    vrmin: Minimum voltage regulator outputs (V).  Typical Value = -6.7.
    """

    ilr : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ka : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kf : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    klr : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pssin : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tb : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tb1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tf : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    uelin : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vamax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vamin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vimax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vimin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
