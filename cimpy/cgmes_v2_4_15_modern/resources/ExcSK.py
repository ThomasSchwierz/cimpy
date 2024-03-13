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
class ExcSK(ExcitationSystemDynamics):
    """
    Slovakian Excitation System Model.  UEL and secondary voltage control are included in this model. When this model is
      used, there cannot be a separate underexcitation limiter or VAr controller model.

    efdmax: Field voltage clipping limit (Efdmax).
    efdmin: Field voltage clipping limit (Efdmin).
    emax: Maximum field voltage output (Emax).  Typical Value = 20.
    emin: Minimum field voltage output (Emin).  Typical Value = -20.
    k: Gain (K).  Typical Value = 1.
    k1: Parameter of underexcitation limit (K1).  Typical Value = 0.1364.
    k2: Parameter of underexcitation limit (K2).  Typical Value = -0.3861.
    kc: PI controller gain (Kc).  Typical Value = 70.
    kce: Rectifier regulation factor (Kce).  Typical Value = 0.
    kd: Exciter internal reactance (Kd).  Typical Value = 0.
    kgob: P controller gain (Kgob).  Typical Value = 10.
    kp: PI controller gain (Kp).  Typical Value = 1.
    kqi: PI controller gain of integral component (Kqi).  Typical Value = 0.
    kqob: Rate of rise of the reactive power (Kqob).
    kqp: PI controller gain (Kqp).  Typical Value = 0.
    nq: Dead band of reactive power (nq).  Determines the range of sensitivity.  Typical Value = 0.001.
    qconoff: Secondary voltage control state (Qc_on_off). true = secondary voltage control is ON false = secondary
      voltage control is OFF. Typical Value = false.
    qz: Desired value (setpoint) of reactive power, manual setting (Qz).
    remote: Selector to apply automatic calculation in secondary controller model. true = automatic calculation is
      activated false = manual set is active; the use of desired value of reactive power (Qz) is required.
      Typical Value = true.
    sbase: Apparent power of the unit (Sbase).  Unit = MVA.  Typical Value = 259.
    tc: PI controller phase lead time constant (Tc).  Typical Value = 8.
    te: Time constant of gain block (Te).  Typical Value = 0.1.
    ti: PI controller phase lead time constant (Ti).  Typical Value = 2.
    tp: Time constant (Tp).  Typical Value = 0.1.
    tr: Voltage transducer time constant (Tr).  Typical Value = 0.01.
    uimax: Maximum error (Uimax).  Typical Value = 10.
    uimin: Minimum error (UImin).  Typical Value = -10.
    urmax: Maximum controller output (URmax).  Typical Value = 10.
    urmin: Minimum controller output (URmin).  Typical Value = -10.
    vtmax: Maximum terminal voltage input (Vtmax).  Determines the range of voltage dead band.  Typical Value = 1.05.
    vtmin: Minimum terminal voltage input (Vtmin).  Determines the range of voltage dead band.  Typical Value = 0.95.
    yp: Maximum output (Yp).  Minimum output = 0.  Typical Value = 1.
    """

    efdmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efdmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    emax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    emin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kce : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kd : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kgob : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kqi : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kqob : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kqp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    nq : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    qconoff : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    qz : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    remote : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    sbase : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    te : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ti : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tp : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tr : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    uimax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    uimin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    urmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    urmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vtmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vtmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    yp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
