"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .AsynchronousMachineDynamics import AsynchronousMachineDynamics

@dataclass
class AsynchronousMachineTimeConstantReactance(AsynchronousMachineDynamics):
    """
    The parameters used for models expressed in time constant reactance form include:

    xs: Synchronous reactance (Xs) (>= X`).  Typical Value = 1.8.
    xp: Transient reactance (unsaturated) (X`) (>=X``).  Typical Value = 0.5.
    xpp: Subtransient reactance (unsaturated) (X``) (> Xl).  Typical Value = 0.2.
    tpo: Transient rotor time constant (T`o) (> T``o).  Typical Value = 5.
    tppo: Subtransient rotor time constant (T``o) (> 0).  Typical Value = 0.03.
    """

    xs : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    xp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    xpp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tpo : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tppo : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
