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
class ExcDC3A(ExcitationSystemDynamics):
    """
    This is modified IEEE DC3A direct current commutator exciters with speed input, and death band.  DC old type 4.

    trh: Rheostat travel time (Trh).  Typical Value = 20.
    ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0.
    kr: Death band (Kr).  If Kr is not zero, the voltage regulator input changes at a constant rate if Verr > Kr or Verr
      < -Kr as per the IEEE (1968) Type 4 model. If Kr is zero, the error signal drives the voltage regulator
      continuously as per the IEEE (1980) DC3 and IEEE (1992, 2005) DC3A models.  Typical Value = 0.
    kv: Fast raise/lower contact setting (Kv).  Typical Value = 0.05.
    vrmax: Maximum voltage regulator output (Vrmax).  Typical Value = 5.
    vrmin: Minimum voltage regulator output (Vrmin).  Typical Value = 0.
    te: Exciter time constant, integration rate associated with exciter control (Te).  Typical Value = 1.83.
    ke: Exciter constant related to self-excited field (Ke).  Typical Value = 1.
    efd1: Exciter voltage at which exciter saturation is defined (Efd1).  Typical Value = 2.6.
    seefd1: Exciter saturation function value at the corresponding exciter voltage, Efd1 (Se[Eefd1]).  Typical Value =
      0.1.
    efd2: Exciter voltage at which exciter saturation is defined (Efd2).  Typical Value = 3.45.
    seefd2: Exciter saturation function value at the corresponding exciter voltage, Efd2 (Se[Efd2]).  Typical Value =
      0.35.
    exclim: (exclim).  IEEE standard is ambiguous about lower limit on exciter output. true = a lower limit of zero is
      applied to integrator output false = a lower limit of zero not applied to integrator output. Typical
      Value = true.
    edfmax: Maximum voltage exciter output limiter (Efdmax).  Typical Value = 99.
    efdmin: Minimum voltage exciter output limiter (Efdmin).  Typical Value = -99.
    efdlim: (Efdlim). true = exciter output limiter is active false = exciter output limiter not active. Typical Value =
      true.
    """

    trh : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ks : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kr : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

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

    edfmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efdmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efdlim : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
