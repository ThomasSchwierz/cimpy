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
class GovGAST1(TurbineGovernorDynamics):
    """
    Modified single shaft gas turbine.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    r: Permanent droop (R).  Typical Value = 0.04.
    t1: Governor mechanism time constant (T1).  T1 represents the natural valve positioning time constant of the
      governor for small disturbances, as seen when rate limiting is not in effect.  Typical Value = 0.5.
    t2: Turbine power time constant (T2).  T2 represents delay due to internal energy storage of the gas turbine engine.
      T2 can be used to give a rough approximation to the delay associated with acceleration of the compressor
      spool of a multi-shaft engine, or with the compressibility of gas in the plenum of the free power turbine
      of an aero-derivative unit, for example.  Typical Value = 0.5.
    t3: Turbine exhaust temperature time constant (T3).  T3 represents delay in the exhaust temperature and load
      limiting system. Typical Value = 3.
    lmax: Ambient temperature load limit (Lmax).  Lmax is the turbine power output corresponding to the limiting exhaust
      gas temperature.  Typical Value = 1.
    kt: Temperature limiter gain (Kt).  Typical Value = 3.
    vmax: Maximum turbine power, PU of MWbase (Vmax).  Typical Value = 1.
    vmin: Minimum turbine power, PU of MWbase (Vmin).  Typical Value = 0.
    fidle: Fuel flow at zero power output (Fidle).  Typical Value = 0.18.
    rmax: Maximum fuel valve opening rate (Rmax).  Unit = PU/sec.  Typical Value = 1.
    loadinc: Valve position change allowed at fast rate (Loadinc).  Typical Value = 0.05.
    tltr: Valve position averaging time constant (Tltr).  Typical Value = 10.
    ltrate: Maximum long term fuel valve opening rate (Ltrate).  Typical Value = 0.02.
    a: Turbine power time constant numerator scale factor (a).  Typical Value = 0.8.
    b: Turbine power time constant denominator scale factor (b).  Typical Value = 1.
    db1: Intentional dead-band width (db1).  Unit = Hz.  Typical Value = 0.
    eps: Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0.
    db2: Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0.
    gv1: Nonlinear gain point 1, PU gv (Gv1).  Typical Value = 0.
    pgv1: Nonlinear gain point 1, PU power (Pgv1).  Typical Value = 0.
    gv2: Nonlinear gain point 2,PU gv (Gv2).  Typical Value = 0.
    pgv2: Nonlinear gain point 2, PU power (Pgv2).  Typical Value = 0.
    gv3: Nonlinear gain point 3, PU gv (Gv3).  Typical Value = 0.
    pgv3: Nonlinear gain point 3, PU power (Pgv3).  Typical Value = 0.
    gv4: Nonlinear gain point 4, PU gv (Gv4).  Typical Value = 0.
    pgv4: Nonlinear gain point 4, PU power (Pgv4).  Typical Value = 0.
    gv5: Nonlinear gain point 5, PU gv (Gv5).  Typical Value = 0.
    pgv5: Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0.
    gv6: Nonlinear gain point 6, PU gv (Gv6).  Typical Value = 0.
    pgv6: Nonlinear gain point 6, PU power (Pgv6).  Typical Value = 0.
    ka: Governor gain (Ka).  Typical Value = 0.
    t4: Governor lead time constant (T4).  Typical Value = 0.
    t5: Governor lag time constant (T5).  Typical Value = 0.
    """

    mwbase : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    r : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    lmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kt : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    fidle : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    loadinc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tltr : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ltrate : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    a : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    b : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    db1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    eps : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    db2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

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

    ka : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t4 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t5 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
