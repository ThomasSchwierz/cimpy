"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .DiscontinuousExcitationControlDynamics import DiscontinuousExcitationControlDynamics

@dataclass
class DiscExcContIEEEDEC1A(DiscontinuousExcitationControlDynamics):
    """
    The class represents IEEE Type DEC1A discontinuous excitation control model that boosts generator excitation to a
      level higher than that demanded by the voltage regulator and stabilizer immediately following a system fault.
      Reference: IEEE Standard 421.5-2005 Section 12.2.

    vtlmt: Voltage reference ().  Typical Value = 1.1.
    vomax: Limiter ().  Typical Value = 0.3.
    vomin: Limiter ().  Typical Value = 0.1.
    ketl: Terminal voltage limiter gain ().  Typical Value = 47.
    vtc: Terminal voltage level reference ().  Typical Value = 0.95.
    val: Regulator voltage reference ().  Typical Value = 5.5.
    esc: Speed change reference ().  Typical Value = 0.0015.
    kan: Discontinuous controller gain ().  Typical Value = 400.
    tan: Discontinuous controller time constant ().  Typical Value = 0.08.
    tw5: DEC washout time constant ().  Typical Value = 5.
    vsmax: Limiter ().  Typical Value = 0.2.
    vsmin: Limiter ().  Typical Value = -0.066.
    td: Time constant ().  Typical Value = 0.03.
    tl1: Time constant ().  Typical Value = 0.025.
    tl2: Time constant ().  Typical Value = 1.25.
    vtm: Voltage limits ().  Typical Value = 1.13.
    vtn: Voltage limits ().  Typical Value = 1.12.
    vanmax: Limiter for Van ().
    """

    vtlmt : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vomax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vomin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ketl : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vtc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    val : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    esc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kan : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tan : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tw5 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vsmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vsmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    td : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tl1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tl2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vtm : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vtn : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vanmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
