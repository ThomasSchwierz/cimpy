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
class ExcANS(ExcitationSystemDynamics):
    """
    Italian excitation system. It represents static field voltage or excitation current feedback excitation system.

    k3: AVR gain (K).  Typical Value = 1000.
    k2: Exciter gain (K).  Typical Value = 20.
    kce: Ceiling factor (K).  Typical Value = 1.
    t3: Time constant (T).  Typical Value = 1.6.
    t2: Time constant (T).  Typical Value = 0.05.
    t1: Time constant (T).  Typical Value = 20.
    blint: Governor Control Flag (BLINT).  0 = lead-lag regulator 1 = proportional integral regulator. Typical Value =
      0.
    kvfif: Rate feedback signal flag (K).  0 = output voltage of the exciter 1 = exciter field current. Typical Value =
      0.
    ifmn: Minimum exciter current (I).  Typical Value = -5.2.
    ifmx: Maximum exciter current (I).  Typical Value = 6.5.
    vrmn: Maximum AVR output (V).  Typical Value = -5.2.
    vrmx: Minimum AVR output (V).  Typical Value = 6.5.
    krvecc: Feedback enabling (K).  0 = Open loop control 1 = Closed loop control. Typical Value = 1.
    tb: Exciter time constant (T).  Typical Value = 0.04.
    """

    k3 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kce : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    blint : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kvfif : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ifmn : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ifmx : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmn : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmx : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    krvecc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tb : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
