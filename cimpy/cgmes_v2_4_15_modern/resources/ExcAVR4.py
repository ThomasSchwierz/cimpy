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
class ExcAVR4(ExcitationSystemDynamics):
    """
    Italian excitation system. It represents static exciter and electric voltage regulator.

    ka: AVR gain (K).  Typical Value = 300.
    vrmn: Maximum AVR output (V).  Typical Value = 0.
    vrmx: Minimum AVR output (V).  Typical Value = 5.
    t1: AVR time constant (T).  Typical Value = 4.8.
    t2: AVR time constant (T).  Typical Value = 1.5.
    t3: AVR time constant (T).  Typical Value = 0.
    t4: AVR time constant (T).  Typical Value = 0.
    ke: Exciter gain (K).  Typical Value = 1.
    vfmx: Maximum exciter output (V).  Typical Value = 5.
    vfmn: Minimum exciter output (V).  Typical Value = 0.
    kif: Exciter internal reactance (K).  Typical Value = 0.
    tif: Exciter current feedback time constant (T).  Typical Value = 0.
    t1if: Exciter current feedback time constant (T).  Typical Value = 60.
    imul: AVR output voltage dependency selector (Imul). true = selector is connected false = selector is not connected.
      Typical Value = true.
    """

    ka : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmn : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmx : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t4 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ke : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vfmx : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vfmn : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kif : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tif : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t1if : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    imul : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
