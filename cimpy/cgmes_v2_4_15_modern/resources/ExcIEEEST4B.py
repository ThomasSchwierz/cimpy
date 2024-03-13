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
class ExcIEEEST4B(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type ST4B model. This model is a variation of the Type ST3A model, with a
      proportional plus integral (PI) regulator block replacing the lag-lead regulator characteristic that is in the
      ST3A model. Both potential and compound source rectifier excitation systems are modeled.  The PI regulator
      blocks have non-windup limits that are represented. The voltage regulator of this model is typically
      implemented digitally.  Reference: IEEE Standard 421.5-2005 Section 7.4.

    kpr: Voltage regulator proportional gain (K).  Typical Value = 10.75.
    kir: Voltage regulator integral gain (K).  Typical Value = 10.75.
    ta: Voltage regulator time constant (T).  Typical Value = 0.02.
    vrmax: Maximum voltage regulator output (V).  Typical Value = 1.
    vrmin: Minimum voltage regulator output (V).  Typical Value = -0.87.
    kpm: Voltage regulator proportional gain output (K).  Typical Value = 1.
    kim: Voltage regulator integral gain output (K).  Typical Value = 0.
    vmmax: Maximum inner loop output (V).  Typical Value = 99.
    vmmin: Minimum inner loop output (V).  Typical Value = -99.
    kg: Feedback gain constant of the inner loop field regulator (K).  Typical Value = 0.
    kp: Potential circuit gain coefficient (K).  Typical Value = 9.3.
    thetap: Potential circuit phase angle (thetap).  Typical Value = 0.
    ki: Potential circuit gain coefficient (K).  Typical Value = 0.
    kc: Rectifier loading factor proportional to commutating reactance (K). Typical Value = 0.113.
    xl: Reactance associated with potential source (X).  Typical Value = 0.124.
    vbmax: Maximum excitation voltage (V).  Typical Value = 11.63.
    """

    kpr : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kir : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kpm : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kim : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vmmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vmmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kg : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    thetap : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ki : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    xl : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vbmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
