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
class ExcIEEEST3A(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type ST3A model.  Some static systems utilize a field voltage control loop
      to linearize the exciter control characteristic. This also makes the output independent of supply source
      variations until supply limitations are reached.  These systems utilize a variety of controlled-rectifier
      designs: full thyristor complements or hybrid bridges in either series or shunt configurations. The power
      source may consist of only a potential source, either fed from the machine terminals or from internal
      windings. Some designs may have compound power sources utilizing both machine potential and current. These
      power sources are represented as phasor combinations of machine terminal current and voltage and are
      accommodated by suitable parameters in model Type ST3A which is represented by ExcIEEEST3A.   Reference: IEEE
      Standard 421.5-2005 Section 7.3.

    vimax: Maximum voltage regulator input limit (V).  Typical Value = 0.2.
    vimin: Minimum voltage regulator input limit (V).  Typical Value = -0.2.
    ka: Voltage regulator gain (K). This is parameter K in the IEEE Std. Typical Value = 200.
    ta: Voltage regulator time constant (T).  Typical Value = 0.
    tb: Voltage regulator time constant (T).  Typical Value = 10.
    tc: Voltage regulator time constant (T).  Typical Value = 1.
    vrmax: Maximum voltage regulator output (V).  Typical Value = 10.
    vrmin: Minimum voltage regulator output (V).  Typical Value = -10.
    km: Forward gain constant of the inner loop field regulator (K).  Typical Value = 7.93.
    tm: Forward time constant of inner loop field regulator (T).  Typical Value = 0.4.
    vmmax: Maximum inner loop output (V).  Typical Value = 1.
    vmmin: Minimum inner loop output (V).  Typical Value = 0.
    kg: Feedback gain constant of the inner loop field regulator (K).  Typical Value = 1.
    kp: Potential circuit gain coefficient (K).  Typical Value = 6.15.
    thetap: Potential circuit phase angle (thetap).  Typical Value = 0.
    ki: Potential circuit gain coefficient (K).  Typical Value = 0.
    kc: Rectifier loading factor proportional to commutating reactance (K). Typical Value = 0.2.
    xl: Reactance associated with potential source (X).  Typical Value = 0.081.
    vbmax: Maximum excitation voltage (V).  Typical Value = 6.9.
    vgmax: Maximum inner loop feedback voltage (V).  Typical Value = 5.8.
    """

    vimax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vimin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ka : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tb : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    km : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tm : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

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



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
