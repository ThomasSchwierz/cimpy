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
class ExcOEX3T(ExcitationSystemDynamics):
    """
    Modified IEEE Type ST1 Excitation System with semi-continuous and acting terminal voltage limiter.

    t1: Time constant (T).
    t2: Time constant (T).
    t3: Time constant (T).
    t4: Time constant (T).
    ka: Gain (K).
    t5: Time constant (T).
    t6: Time constant (T).
    vrmax: Limiter (V).
    vrmin: Limiter (V).
    te: Time constant (T).
    kf: Gain (K).
    tf: Time constant (T).
    kc: Gain (K).
    kd: Gain (K).
    ke: Gain (K).
    e1: Saturation parameter (E).
    see1: Saturation parameter (S(E)).
    e2: Saturation parameter (E).
    see2: Saturation parameter (S(E)).
    """

    t1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t4 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ka : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t5 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t6 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    te : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kf : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tf : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kd : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ke : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    e1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    see1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    e2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    see2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
