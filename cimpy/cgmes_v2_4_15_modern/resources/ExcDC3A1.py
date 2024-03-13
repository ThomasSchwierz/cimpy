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
class ExcDC3A1(ExcitationSystemDynamics):
    """
    This is modified old IEEE type 3 excitation system.

    ka: Voltage regulator gain (Ka).  Typical Value = 300.
    ta: Voltage regulator time constant (Ta).  Typical Value = 0.01.
    vrmax: Maximum voltage regulator output (Vrmax).  Typical Value = 5.
    vrmin: Minimum voltage regulator output (Vrmin).  Typical Value = 0.
    te: Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 1.83.
    kf: Excitation control system stabilizer gain (Kf).  Typical Value = 0.1.
    tf: Excitation control system stabilizer time constant (Tf).  Typical Value = 0.675.
    kp: Potential circuit gain coefficient (Kp).  Typical Value = 4.37.
    ki: Potential circuit gain coefficient (Ki).  Typical Value = 4.83.
    vbmax: Available exciter voltage limiter (Vbmax).  Typical Value = 11.63.
    exclim: (exclim). true = lower limit of zero is applied to integrator output false = lower limit of zero not applied
      to integrator output. Typical Value = true.
    ke: Exciter constant related to self-excited field (Ke).  Typical Value = 1.
    vb1max: Available exciter voltage limiter (Vb1max).  Typical Value = 11.63.
    vblim: Vb limiter indicator. true = exciter Vbmax limiter is active false = Vb1max is active.  Typical Value = true.
    """

    ka : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    te : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kf : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tf : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ki : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vbmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    exclim : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ke : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vb1max : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vblim : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
