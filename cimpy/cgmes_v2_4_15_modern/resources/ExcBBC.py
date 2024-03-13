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
class ExcBBC(ExcitationSystemDynamics):
    """
    Transformer fed static excitation system (static with ABB regulator). This model represents a static excitation
      system in which a gated thyristor bridge fed by a transformer at the main generator terminals feeds the main
      generator directly.

    t1: Controller time constant (T1).  Typical Value = 6.
    t2: Controller time constant (T2).  Typical Value = 1.
    t3: Lead/lag time constant (T3).  Typical Value = 0.05.
    t4: Lead/lag time constant (T4).  Typical Value = 0.01.
    k: Steady state gain (K).  Typical Value = 300.
    vrmin: Minimum control element output (Vrmin).  Typical Value = -5.
    vrmax: Maximum control element output (Vrmax).  Typical Value = 5.
    efdmin: Minimum open circuit exciter voltage (Efdmin).  Typical Value = -5.
    efdmax: Maximum open circuit exciter voltage (Efdmax).  Typical Value = 5.
    xe: Effective excitation transformer reactance (Xe).  Typical Value = 0.05.
    switch: Supplementary signal routing selector (switch). true = Vs connected to 3rd summing point false =  Vs
      connected to 1st summing point (see diagram). Typical Value = true.
    """

    t1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t4 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efdmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efdmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    xe : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    switch : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
