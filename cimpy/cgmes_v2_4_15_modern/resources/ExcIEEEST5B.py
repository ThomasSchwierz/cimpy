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
class ExcIEEEST5B(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type ST5B model. The Type ST5B excitation system is a variation of the Type
      ST1A model, with alternative overexcitation and underexcitation inputs and additional limits.  Reference: IEEE
      Standard 421.5-2005 Section 7.5.   Note: the block diagram in the IEEE 421.5 standard has input signal Vc and
      does not indicate the summation point with Vref. The implementation of the ExcIEEEST5B shall consider
      summation point with Vref.

    kr: Regulator gain (K).  Typical Value = 200.
    t1: Firing circuit time constant (T1).  Typical Value = 0.004.
    kc: Rectifier regulation factor (K).  Typical Value = 0.004.
    vrmax: Maximum voltage regulator output (V).  Typical Value = 5.
    vrmin: Minimum voltage regulator output (V).  Typical Value = -4.
    tc1: Regulator lead time constant (T).  Typical Value = 0.8.
    tb1: Regulator lag time constant (T).  Typical Value = 6.
    tc2: Regulator lead time constant (T).  Typical Value = 0.08.
    tb2: Regulator lag time constant (T).  Typical Value = 0.01.
    toc1: OEL lead time constant (T).  Typical Value = 0.1.
    tob1: OEL lag time constant (T).  Typical Value = 2.
    toc2: OEL lead time constant (T).  Typical Value = 0.08.
    tob2: OEL lag time constant (T).  Typical Value = 0.08.
    tuc1: UEL lead time constant (T).  Typical Value = 2.
    tub1: UEL lag time constant (T).  Typical Value = 10.
    tuc2: UEL lead time constant (T).  Typical Value = 0.1.
    tub2: UEL lag time constant (T).  Typical Value = 0.05.
    """

    kr : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tb1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tb2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    toc1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tob1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    toc2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tob2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tuc1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tub1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tuc2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tub2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
