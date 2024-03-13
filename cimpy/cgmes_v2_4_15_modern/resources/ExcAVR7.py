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
class ExcAVR7(ExcitationSystemDynamics):
    """
    IVO excitation system.

    k1: Gain (K1).  Typical Value = 1.
    a1: Lead coefficient (A1).  Typical Value = 0.5.
    a2: Lag coefficient (A2).  Typical Value = 0.5.
    t1: Lead time constant (T1).  Typical Value = 0.05.
    t2: Lag time constant (T2).  Typical Value = 0.1.
    vmax1: Lead-lag max. limit (Vmax1).  Typical Value = 5.
    vmin1: Lead-lag min. limit (Vmin1).  Typical Value = -5.
    k3: Gain (K3).  Typical Value = 3.
    a3: Lead coefficient (A3).  Typical Value = 0.5.
    a4: Lag coefficient (A4).  Typical Value = 0.5.
    t3: Lead time constant (T3).  Typical Value = 0.1.
    t4: Lag time constant (T4).  Typical Value = 0.1.
    vmax3: Lead-lag max. limit (Vmax3).  Typical Value = 5.
    vmin3: Lead-lag min. limit (Vmin3).  Typical Value = -5.
    k5: Gain (K5).  Typical Value = 1.
    a5: Lead coefficient (A5).  Typical Value = 0.5.
    a6: Lag coefficient (A6).  Typical Value = 0.5.
    t5: Lead time constant (T5).  Typical Value = 0.1.
    t6: Lag time constant (T6).  Typical Value = 0.1.
    vmax5: Lead-lag max. limit (Vmax5).  Typical Value = 5.
    vmin5: Lead-lag min. limit (Vmin5).  Typical Value = -2.
    """

    k1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    a1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    a2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vmax1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vmin1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k3 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    a3 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    a4 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t4 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vmax3 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vmin3 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k5 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    a5 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    a6 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t5 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t6 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vmax5 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vmin5 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
