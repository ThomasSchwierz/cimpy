"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .LoadDynamics import LoadDynamics

@dataclass
class LoadComposite(LoadDynamics):
    """
    This models combines static load and induction motor load effects. The dynamics of the motor are simplified by
      linearizing the induction machine equations.

    epvs: Active load-voltage dependence index (static) (Epvs).  Typical Value = 0.7.
    epfs: Active load-frequency dependence index (static) (Epfs).  Typical Value = 1.5.
    eqvs: Reactive load-voltage dependence index (static) (Eqvs).  Typical Value = 2.
    eqfs: Reactive load-frequency dependence index (static) (Eqfs).  Typical Value = 0.
    epvd: Active load-voltage dependence index (dynamic) (Epvd).  Typical Value = 0.7.
    epfd: Active load-frequency dependence index (dynamic) (Epfd).  Typical Value = 1.5.
    eqvd: Reactive load-voltage dependence index (dynamic) (Eqvd).  Typical Value = 2.
    eqfd: Reactive load-frequency dependence index (dynamic) (Eqfd).  Typical Value = 0.
    lfrac: Loading factor - ratio of initial P to motor MVA base (Lfrac).  Typical Value = 0.8.
    h: Inertia constant (H).  Typical Value = 2.5.
    pfrac: Fraction of constant-power load to be represented by this motor model (Pfrac) (>=0.0 and <=1.0).  Typical
      Value = 0.5.
    """

    epvs : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    epfs : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    eqvs : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    eqfs : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    epvd : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    epfd : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    eqvd : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    eqfd : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    lfrac : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    h : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pfrac : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
