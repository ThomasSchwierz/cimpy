"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics

@dataclass
class PssSB4(PowerSystemStabilizerDynamics):
    """
    Power sensitive stabilizer model.

    tt: Time constant (Tt).
    kx: Gain (Kx).
    tx2: Time constant (Tx2).
    ta: Time constant (Ta).
    tx1: Reset time constant (Tx1).
    tb: Time constant (Tb).
    tc: Time constant (Tc).
    td: Time constant (Td).
    te: Time constant (Te).
    vsmax: Limiter (Vsmax).
    vsmin: Limiter (Vsmin).
    """

    tt : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kx : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tx2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tx1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tb : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    td : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    te : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vsmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vsmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
