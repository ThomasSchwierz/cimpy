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
class ExcSCRX(ExcitationSystemDynamics):
    """
    Simple excitation system model representing generic characteristics of many excitation systems; intended for use
      where negative field current may be a problem.

    tatb: Ta/Tb - gain reduction ratio of lag-lead element (TaTb). The parameter Ta is not defined explicitly.  Typical
      Value = 0.1.
    tb: Denominator time constant of lag-lead block (Tb).  Typical Value = 10.
    k: Gain (K) (>0).  Typical Value = 200.
    te: Time constant of gain block (Te) (>0).  Typical Value = 0.02.
    emin: Minimum field voltage output (Emin).  Typical Value = 0.
    emax: Maximum field voltage output (Emax).  Typical Value = 5.
    cswitch: Power source switch (Cswitch). true = fixed voltage of 1.0 PU false = generator terminal voltage.
    rcrfd: Rc/Rfd - ratio of field discharge resistance to field winding resistance (RcRfd).  Typical Value = 0.
    """

    tatb : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tb : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    te : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    emin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    emax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    cswitch : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rcrfd : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
