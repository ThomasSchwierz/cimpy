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
class ExcST6B(ExcitationSystemDynamics):
    """
    Modified IEEE ST6B static excitation system with PID controller and optional inner feedbacks loop.

    ilr: Exciter output current limit reference (Ilr).  Typical Value = 4.164.
    k1: Selector (K1). true = feedback is from Ifd false = feedback is not from Ifd. Typical Value = true.
    kcl: Exciter output current limit adjustment (Kcl).  Typical Value = 1.0577.
    kff: Pre-control gain constant of the inner loop field regulator (Kff).  Typical Value = 1.
    kg: Feedback gain constant of the inner loop field regulator (Kg).  Typical Value = 1.
    kia: Voltage regulator integral gain (Kia).  Typical Value = 45.094.
    klr: Exciter output current limit adjustment (Kcl).  Typical Value = 17.33.
    km: Forward gain constant of the inner loop field regulator (Km).  Typical Value = 1.
    kpa: Voltage regulator proportional gain (Kpa).  Typical Value = 18.038.
    kvd: Voltage regulator derivative gain (Kvd).  Typical Value = 0.
    oelin: OEL input selector (OELin). Typical Value = noOELinput.
    tg: Feedback time constant of inner loop field voltage regulator (Tg).  Typical Value = 0.02.
    ts: Rectifier firing time constant (Ts).  Typical Value = 0.
    tvd: Voltage regulator derivative gain (Tvd).  Typical Value = 0.
    vamax: Maximum voltage regulator output (Vamax).  Typical Value = 4.81.
    vamin: Minimum voltage regulator output (Vamin).  Typical Value = -3.85.
    vilim: Selector (Vilim). true = Vimin-Vimax limiter is active false = Vimin-Vimax limiter is not active. Typical
      Value = true.
    vimax: Maximum voltage regulator input limit (Vimax).  Typical Value = 10.
    vimin: Minimum voltage regulator input limit (Vimin).  Typical Value = -10.
    vmult: Selector (Vmult). true = multiply regulator output by terminal voltage false = do not multiply regulator
      output by terminal voltage.  Typical Value = true.
    vrmax: Maximum voltage regulator output (Vrmax).  Typical Value = 4.81.
    vrmin: Minimum voltage regulator output (Vrmin).  Typical Value = -3.85.
    xc: Excitation source reactance (Xc).  Typical Value = 0.05.
    """

    ilr : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k1 : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kcl : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kff : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kg : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kia : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    klr : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    km : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kpa : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kvd : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    oelin : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tg : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ts : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tvd : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vamax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vamin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vilim : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vimax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vimin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vmult : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

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
