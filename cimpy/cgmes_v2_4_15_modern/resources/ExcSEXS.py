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
class ExcSEXS(ExcitationSystemDynamics):
    """
    Simplified Excitation System Model.

    tatb: Ta/Tb - gain reduction ratio of lag-lead element (TaTb).  Typical Value = 0.1.
    tb: Denominator time constant of lag-lead block (Tb).  Typical Value = 10.
    k: Gain (K) (>0).  Typical Value = 100.
    te: Time constant of gain block (Te).  Typical Value = 0.05.
    emin: Minimum field voltage output (Emin).  Typical Value = -5.
    emax: Maximum field voltage output (Emax).  Typical Value = 5.
    kc: PI controller gain (Kc).  Typical Value = 0.08.
    tc: PI controller phase lead time constant (Tc).  Typical Value = 0.
    efdmin: Field voltage clipping minimum limit (Efdmin).  Typical Value = -5.
    efdmax: Field voltage clipping maximum limit (Efdmax).  Typical Value = 5.
    """

    tatb : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tb : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    te : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    emin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    emax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efdmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efdmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
