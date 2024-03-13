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
class ExcIEEEDC3A(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type DC3A model. This model represents represent older systems, in
      particular those dc commutator exciters with non-continuously acting regulators that were commonly used before
      the development of the continuously acting varieties.  These systems respond at basically two different rates,
      depending upon the magnitude of voltage error. For small errors, adjustment is made periodically with a signal
      to a motor-operated rheostat. Larger errors cause resistors to be quickly shorted or inserted and a strong
      forcing signal applied to the exciter. Continuous motion of the motor-operated rheostat occurs for these
      larger error signals, even though it is bypassed by contactor action.   Reference: IEEE Standard 421.5-2005
      Section 5.3.

    trh: Rheostat travel time (T).  Typical Value = 20.
    kv: Fast raise/lower contact setting (K).  Typical Value = 0.05.
    vrmax: Maximum voltage regulator output (V).  Typical Value = 1.
    vrmin: Minimum voltage regulator output (V).  Typical Value = 0.
    te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 0.5.
    ke: Exciter constant related to self-excited field (K).  Typical Value = 0.05.
    efd1: Exciter voltage at which exciter saturation is defined (E).  Typical Value = 3.375.
    seefd1: Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.267.
    efd2: Exciter voltage at which exciter saturation is defined (E).  Typical Value = 3.15.
    seefd2: Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.068.
    exclim: (exclim).  IEEE standard is ambiguous about lower limit on exciter output. true = a lower limit of zero is
      applied to integrator output false = a lower limit of zero is not applied to integrator output.
      Typical Value = true.
    """

    trh : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kv : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    te : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ke : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efd1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    seefd1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efd2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    seefd2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    exclim : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
