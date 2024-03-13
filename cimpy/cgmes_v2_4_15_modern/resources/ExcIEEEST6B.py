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
class ExcIEEEST6B(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type ST6B model. This model consists of a PI voltage regulator with an
      inner loop field voltage regulator and pre-control. The field voltage regulator implements a proportional
      control. The pre-control and the delay in the feedback circuit increase the dynamic response.  Reference: IEEE
      Standard 421.5-2005 Section 7.6.

    ilr: Exciter output current limit reference (I).  Typical Value = 4.164.
    kci: Exciter output current limit adjustment (K).  Typical Value = 1.0577.
    kff: Pre-control gain constant of the inner loop field regulator (K). Typical Value = 1.
    kg: Feedback gain constant of the inner loop field regulator (K).  Typical Value = 1.
    kia: Voltage regulator integral gain (K).  Typical Value = 45.094.
    klr: Exciter output current limiter gain (K).  Typical Value = 17.33.
    km: Forward gain constant of the inner loop field regulator (K).  Typical Value = 1.
    kpa: Voltage regulator proportional gain (K).  Typical Value = 18.038.
    oelin: OEL input selector (OELin). Typical Value = noOELinput.
    tg: Feedback time constant of inner loop field voltage regulator (T). Typical Value = 0.02.
    vamax: Maximum voltage regulator output (V).  Typical Value = 4.81.
    vamin: Minimum voltage regulator output (V).  Typical Value = -3.85.
    vrmax: Maximum voltage regulator output (V).  Typical Value = 4.81.
    vrmin: Minimum voltage regulator output (V).  Typical Value = -3.85.
    """

    ilr : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kci : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kff : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kg : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kia : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    klr : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    km : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kpa : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    oelin : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tg : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vamax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vamin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
