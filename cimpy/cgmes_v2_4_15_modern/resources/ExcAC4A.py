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
class ExcAC4A(ExcitationSystemDynamics):
    """
    Modified IEEE AC4A alternator-supplied rectifier excitation system with different minimum controller output.

    vimax: Maximum voltage regulator input limit (Vimax).  Typical Value = 10.
    vimin: Minimum voltage regulator input limit (Vimin).  Typical Value = -10.
    tc: Voltage regulator time constant (Tc).  Typical Value = 1.
    tb: Voltage regulator time constant (Tb).  Typical Value = 10.
    ka: Voltage regulator gain (Ka).  Typical Value = 200.
    ta: Voltage regulator time constant (Ta).  Typical Value = 0.015.
    vrmax: Maximum voltage regulator output (Vrmax).  Typical Value = 5.64.
    vrmin: Minimum voltage regulator output (Vrmin).  Typical Value = -4.53.
    kc: Rectifier loading factor proportional to commutating reactance (Kc).  Typical Value = 0.
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



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
