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
class ExcREXS(ExcitationSystemDynamics):
    """
    General Purpose Rotating Excitation System Model.  This model can be used to represent a wide range of excitation
      systems whose DC power source is an AC or DC generator. It encompasses IEEE type AC1, AC2, DC1, and DC2
      excitation system models.

    e1: Field voltage value 1 (E1).  Typical Value = 3.
    e2: Field voltage value 2 (E2).  Typical Value = 4.
    fbf: Rate feedback signal flag (Fbf). Typical Value = fieldCurrent.
    flimf: Limit type flag (Flimf).  Typical Value = 0.
    kc: Rectifier regulation factor (Kc).  Typical Value = 0.05.
    kd: Exciter regulation factor (Kd).  Typical Value = 2.
    ke: Exciter field proportional constant (Ke).  Typical Value = 1.
    kefd: Field voltage feedback gain (Kefd).  Typical Value = 0.
    kf: Rate feedback gain (Kf).  Typical Value = 0.05.
    kh: Field voltage controller feedback gain (Kh).  Typical Value = 0.
    kii: Field Current Regulator Integral Gain (Kii).  Typical Value = 0.
    kip: Field Current Regulator Proportional Gain (Kip).  Typical Value = 1.
    ks: Coefficient to allow different usage of the model-speed coefficient (Ks).  Typical Value = 0.
    kvi: Voltage Regulator Integral Gain (Kvi).  Typical Value = 0.
    kvp: Voltage Regulator Proportional Gain (Kvp).  Typical Value = 2800.
    kvphz: V/Hz limiter gain (Kvphz).  Typical Value = 0.
    nvphz: Pickup speed of V/Hz limiter (Nvphz).  Typical Value = 0.
    se1: Saturation factor at E1 (Se1).  Typical Value = 0.0001.
    se2: Saturation factor at E2 (Se2).  Typical Value = 0.001.
    ta: Voltage Regulator time constant (Ta).  Typical Value = 0.01.
    tb1: Lag time constant (Tb1).  Typical Value = 0.
    tb2: Lag time constant (Tb2).  Typical Value = 0.
    tc1: Lead time constant (Tc1).  Typical Value = 0.
    tc2: Lead time constant (Tc2).  Typical Value = 0.
    te: Exciter field time constant (Te).  Typical Value = 1.2.
    tf: Rate feedback time constant (Tf).  Typical Value = 1.
    tf1: Feedback lead time constant (Tf1).  Typical Value = 0.
    tf2: Feedback lag time constant (Tf2).  Typical Value = 0.
    tp: Field current Bridge time constant (Tp).  Typical Value = 0.
    vcmax: Maximum compounding voltage (Vcmax).  Typical Value = 0.
    vfmax: Maximum Exciter Field Current (Vfmax).  Typical Value = 47.
    vfmin: Minimum Exciter Field Current (Vfmin).  Typical Value = -20.
    vimax: Voltage Regulator Input Limit (Vimax).  Typical Value = 0.1.
    vrmax: Maximum controller output (Vrmax).  Typical Value = 47.
    vrmin: Minimum controller output (Vrmin).  Typical Value = -20.
    xc: Exciter compounding reactance (Xc).  Typical Value = 0.
    """

    e1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    e2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    fbf : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    flimf : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kd : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ke : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kefd : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kf : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kh : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kii : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kip : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ks : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kvi : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kvp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kvphz : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    nvphz : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    se1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    se2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tb1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tb2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    te : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tf : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tf1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tf2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tp : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vcmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vfmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vfmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vimax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    xc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
