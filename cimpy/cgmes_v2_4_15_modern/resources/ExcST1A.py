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
class ExcST1A(ExcitationSystemDynamics):
    """
    Modification of an old IEEE ST1A static excitation system without overexcitation limiter (OEL) and underexcitation
      limiter (UEL).

    vimax: Maximum voltage regulator input limit (Vimax).  Typical Value = 999.
    vimin: Minimum voltage regulator input limit (Vimin).  Typical Value = -999.
    tc: Voltage regulator time constant (Tc).  Typical Value = 1.
    tb: Voltage regulator time constant (Tb).  Typical Value = 10.
    ka: Voltage regulator gain (Ka).  Typical Value = 190.
    ta: Voltage regulator time constant (Ta).  Typical Value = 0.02.
    vrmax: Maximum voltage regulator outputs (Vrmax).  Typical Value = 7.8.
    vrmin: Minimum voltage regulator outputs (Vrmin).  Typical Value = -6.7.
    kc: Rectifier loading factor proportional to commutating reactance (Kc). Typical Value = 0.05.
    kf: Excitation control system stabilizer gains (Kf).  Typical Value = 0.
    tf: Excitation control system stabilizer time constant (Tf).  Typical Value = 1.
    tc1: Voltage regulator time constant (Tc).  Typical Value = 0.
    tb1: Voltage regulator time constant (Tb).  Typical Value = 0.
    vamax: Maximum voltage regulator output (Vamax).  Typical Value = 999.
    vamin: Minimum voltage regulator output (Vamin).  Typical Value = -999.
    ilr: Exciter output current limit reference (Ilr).  Typical Value = 0.
    klr: Exciter output current limiter gain (Klr).  Typical Value = 0.
    xe: Excitation xfmr effective reactance (Xe).  Typical Value = 0.04.
    """

    vimax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vimin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tb : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ka : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kf : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tf : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tb1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vamax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vamin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ilr : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    klr : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    xe : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
