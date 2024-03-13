"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .TurbineGovernorDynamics import TurbineGovernorDynamics

@dataclass
class GovHydroR(TurbineGovernorDynamics):
    """
    Fourth order lead-lag governor and hydro turbine.

    mwbase: Base for power values (MWbase) (>0).  Unit = MW.
    pmax: Maximum gate opening, PU of MWbase (Pmax).  Typical Value = 1.
    pmin: Minimum gate opening, PU of MWbase (Pmin).  Typical Value = 0.
    r: Steady-state droop (R).  Typical Value = 0.05.
    td: Input filter time constant (Td).  Typical Value = 0.05.
    t1: Lead time constant 1 (T1).  Typical Value = 1.5.
    t2: Lag time constant 1 (T2).  Typical Value = 0.1.
    t3: Lead time constant 2 (T3).  Typical Value = 1.5.
    t4: Lag time constant 2 (T4).  Typical Value = 0.1.
    t5: Lead time constant 3 (T5).  Typical Value = 0.
    t6: Lag time constant 3 (T6).  Typical Value = 0.05.
    t7: Lead time constant 4 (T7).  Typical Value = 0.
    t8: Lag time constant 4 (T8).  Typical Value = 0.05.
    tp: Gate servo time constant (Tp).  Typical Value = 0.05.
    velop: Maximum gate opening velocity (Velop).  Unit = PU/sec.  Typical Value = 0.2.
    velcl: Maximum gate closing velocity (Velcl).  Unit = PU/sec.  Typical Value = -0.2.
    ki: Integral gain (Ki).  Typical Value = 0.5.
    kg: Gate servo gain (Kg).  Typical Value = 2.
    gmax: Maximum governor output (Gmax).  Typical Value = 1.05.
    gmin: Minimum governor output (Gmin).  Typical Value = -0.05.
    tt: Power feedback time constant (Tt).  Typical Value = 0.
    inputSignal: Input signal switch (Flag). true = Pe input is used false = feedback is received from CV. Flag is
      normally dependent on Tt.  If Tf is zero, Flag is set to false. If Tf is not zero, Flag is set to
      true.  Typical Value = true.
    db1: Intentional dead-band width (db1).  Unit = Hz.  Typical Value = 0.
    eps: Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0.
    db2: Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0.
    tw: Water inertia time constant (Tw).  Typical Value = 1.
    at: Turbine gain (At).  Typical Value = 1.2.
    dturb: Turbine damping factor (Dturb).  Typical Value = 0.2.
    qnl: No-load turbine flow at nominal head (Qnl).  Typical Value = 0.08.
    h0: Turbine nominal head (H0).  Typical Value = 1.
    gv1: Nonlinear gain point 1, PU gv (Gv1).  Typical Value = 0.
    pgv1: Nonlinear gain point 1, PU power (Pgv1).  Typical Value = 0.
    gv2: Nonlinear gain point 2, PU gv (Gv2).  Typical Value = 0.
    pgv2: Nonlinear gain point 2, PU power (Pgv2).  Typical Value = 0.
    gv3: Nonlinear gain point 3, PU gv (Gv3).  Typical Value = 0.
    pgv3: Nonlinear gain point 3, PU power (Pgv3).  Typical Value = 0.
    gv4: Nonlinear gain point 4, PU gv (Gv4).  Typical Value = 0.
    pgv4: Nonlinear gain point 4, PU power (Pgv4).  Typical Value = 0.
    gv5: Nonlinear gain point 5, PU gv (Gv5).  Typical Value = 0.
    pgv5: Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0.
    gv6: Nonlinear gain point 6, PU gv (Gv6).  Typical Value = 0.
    pgv6: Nonlinear gain point 6, PU power (Pgv6).  Typical Value = 0.
    """

    mwbase : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    r : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    td : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t4 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t5 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t6 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t7 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t8 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tp : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    velop : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    velcl : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ki : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kg : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    gmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    gmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tt : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    inputSignal : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    db1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    eps : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    db2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tw : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    at : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    dturb : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    qnl : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    h0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    gv1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pgv1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    gv2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pgv2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    gv3 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pgv3 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    gv4 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pgv4 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    gv5 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pgv5 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    gv6 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pgv6 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
