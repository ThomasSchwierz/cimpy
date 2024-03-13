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
class ExcCZ(ExcitationSystemDynamics):
    """
    Czech Proportion/Integral Exciter.

    kp: Regulator proportional gain (Kp).
    tc: Regulator integral time constant (Tc).
    vrmax: Voltage regulator maximum limit (Vrmax).
    vrmin: Voltage regulator minimum limit (Vrmin).
    ka: Regulator gain (Ka).
    ta: Regulator time constant (Ta).
    ke: Exciter constant related to self-excited field (Ke).
    te: Exciter time constant, integration rate associated with exciter control (Te).
    efdmax: Exciter output maximum limit (Efdmax).
    efdmin: Exciter output minimum limit (Efdmin).
    """

    kp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ka : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ke : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    te : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efdmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efdmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
