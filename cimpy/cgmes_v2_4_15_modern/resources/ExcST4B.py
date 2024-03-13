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
class ExcST4B(ExcitationSystemDynamics):
    """
    Modified IEEE ST4B static excitation system with maximum inner loop feedback gain .

    kpr: Voltage regulator proportional gain (Kpr).  Typical Value = 10.75.
    kir: Voltage regulator integral gain (Kir).  Typical Value = 10.75.
    ta: Voltage regulator time constant (Ta).  Typical Value = 0.02.
    vrmax: Maximum voltage regulator output (Vrmax).  Typical Value = 1.
    vrmin: Minimum voltage regulator output (Vrmin).  Typical Value = -0.87.
    kpm: Voltage regulator proportional gain output (Kpm).  Typical Value = 1.
    kim: Voltage regulator integral gain output (Kim).  Typical Value = 0.
    vmmax: Maximum inner loop output (Vmmax).  Typical Value = 99.
    vmmin: Minimum inner loop output (Vmmin).  Typical Value = -99.
    kg: Feedback gain constant of the inner loop field regulator (Kg). Typical Value = 0.
    kp: Potential circuit gain coefficient (Kp).  Typical Value = 9.3.
    thetap: Potential circuit phase angle (thetap).  Typical Value = 0.
    ki: Potential circuit gain coefficient (Ki).  Typical Value = 0.
    kc: Rectifier loading factor proportional to commutating reactance (Kc). Typical Value = 0.113.
    xl: Reactance associated with potential source (Xl).  Typical Value = 0.124.
    vbmax: Maximum excitation voltage (Vbmax).  Typical Value = 11.63.
    vgmax: Maximum inner loop feedback voltage (Vgmax).  Typical Value = 5.8.
    uel: Selector (Uel). true = UEL is part of block diagram false = UEL is not part of block diagram.  Typical Value =
      false.
    lvgate: Selector (LVgate). true = LVgate is part of the block diagram false = LVgate is not part of the block
      diagram.  Typical Value = false.
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

    vgmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    uel : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    lvgate : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
