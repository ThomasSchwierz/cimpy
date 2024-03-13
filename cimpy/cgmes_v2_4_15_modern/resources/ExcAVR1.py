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
class ExcAVR1(ExcitationSystemDynamics):
    """
    Italian excitation system corresponding to IEEE (1968) Type 1 Model. It represents exciter dynamo and
      electromechanical regulator.

    ka: AVR gain (K).  Typical Value = 500.
    vrmn: Maximum AVR output (V).  Typical Value = -6.
    vrmx: Minimum AVR output (V).  Typical Value = 7.
    ta: AVR time constant (T).  Typical Value = 0.2.
    tb: AVR time constant (T).  Typical Value = 0.
    te: Exciter time constant (T).  Typical Value = 1.
    e1: Field voltage value 1  (E1).  Typical Value = 4.18.
    se1: Saturation factor at E1 (S(E1)).  Typical Value = 0.1.
    e2: Field voltage value 2 (E2).  Typical Value = 3.14.
    se2: Saturation factor at E2 (S(E2)).  Typical Value = 0.03.
    kf: Rate feedback gain (K).  Typical Value = 0.02.
    tf: Rate feedback time constant (T).  Typical Value = 1.
    """

    ka : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmn : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmx : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tb : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    te : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    e1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    se1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    e2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    se2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kf : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tf : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
