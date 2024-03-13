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
class GovHydroWEH(TurbineGovernorDynamics):
    """
    Woodward Electric Hydro Governor Model.

    mwbase: Base for power values (MWbase) (>0).  Unit = MW.
    rpg: Permanent droop for governor output feedback (R-Perm-Gate).
    rpp: Permanent droop for electrical power feedback (R-Perm-Pe).
    tpe: Electrical power droop time constant (Tpe).
    kp: Derivative control gain (Kp).
    ki: Derivative controller Integral gain (Ki).
    kd: Derivative controller derivative gain (Kd).
    td: Derivative controller time constant to limit the derivative characteristic beyond a breakdown frequency to avoid
      amplification of high-frequency noise (Td).
    tp: Pilot Valve time lag time constant (Tp).
    tdv: Distributive Valve time lag time constant (Tdv).
    tg: Value to allow the Distribution valve controller to advance beyond the gate movement rate limit (Tg).
    gtmxop: Maximum gate opening rate (Gtmxop).
    gtmxcl: Maximum gate closing rate (Gtmxcl).
    gmax: Maximum Gate Position (Gmax).
    gmin: Minimum Gate Position (Gmin).
    dturb: Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed (PU).
    tw: Water inertia time constant (Tw) (>0).
    db: Speed Dead Band (db).
    dpv: Value to allow the Pilot valve controller to advance beyond the gate limits (Dpv).
    dicn: Value to allow the integral controller to advance beyond the gate limits (Dicn).
    feedbackSignal: Feedback signal selection (Sw). true = PID Output (if R-Perm-Gate=droop and R-Perm-Pe=0) false =
      Electrical Power (if R-Perm-Gate=0 and R-Perm-Pe=droop) or false = Gate Position (if R-Perm-
      Gate=droop and R-Perm-Pe=0).
    gv1: Gate 1 (Gv1).  Gate Position value for point 1 for lookup table representing water flow through the turbine as
      a function of gate position to produce steady state flow.
    gv2: Gate 2 (Gv2).  Gate Position value for point 2 for lookup table representing water flow through the turbine as
      a function of gate position to produce steady state flow.
    gv3: Gate 3 (Gv3).  Gate Position value for point 3 for lookup table representing water flow through the turbine as
      a function of gate position to produce steady state flow.
    gv4: Gate 4 (Gv4).  Gate Position value for point 4 for lookup table representing water flow through the turbine as
      a function of gate position to produce steady state flow.
    gv5: Gate 5 (Gv5).  Gate Position value for point 5 for lookup table representing water flow through the turbine as
      a function of gate position to produce steady state flow.
    fl1: Flow Gate 1 (Fl1).  Flow value for gate position point 1 for lookup table representing water flow through the
      turbine as a function of gate position to produce steady state flow.
    fl2: Flow Gate 2 (Fl2).  Flow value for gate position point 2 for lookup table representing water flow through the
      turbine as a function of gate position to produce steady state flow.
    fl3: Flow Gate 3 (Fl3).  Flow value for gate position point 3 for lookup table representing water flow through the
      turbine as a function of gate position to produce steady state flow.
    fl4: Flow Gate 4 (Fl4).  Flow value for gate position point 4 for lookup table representing water flow through the
      turbine as a function of gate position to produce steady state flow.
    fl5: Flow Gate 5 (Fl5).  Flow value for gate position point 5 for lookup table representing water flow through the
      turbine as a function of gate position to produce steady state flow.
    fp1: Flow P1 (Fp1).  Turbine Flow value for point 1 for lookup table representing per unit mechanical power on
      machine MVA rating as a function of turbine flow.
    fp2: Flow P2 (Fp2).  Turbine Flow value for point 2 for lookup table representing per unit mechanical power on
      machine MVA rating as a function of turbine flow.
    fp3: Flow P3 (Fp3).  Turbine Flow value for point 3 for lookup table representing per unit mechanical power on
      machine MVA rating as a function of turbine flow.
    fp4: Flow P4 (Fp4).  Turbine Flow value for point 4 for lookup table representing per unit mechanical power on
      machine MVA rating as a function of turbine flow.
    fp5: Flow P5 (Fp5).  Turbine Flow value for point 5 for lookup table representing per unit mechanical power on
      machine MVA rating as a function of turbine flow.
    fp6: Flow P6 (Fp6).  Turbine Flow value for point 6 for lookup table representing per unit mechanical power on
      machine MVA rating as a function of turbine flow.
    fp7: Flow P7 (Fp7).  Turbine Flow value for point 7 for lookup table representing per unit mechanical power on
      machine MVA rating as a function of turbine flow.
    fp8: Flow P8 (Fp8).  Turbine Flow value for point 8 for lookup table representing per unit mechanical power on
      machine MVA rating as a function of turbine flow.
    fp9: Flow P9 (Fp9).  Turbine Flow value for point 9 for lookup table representing per unit mechanical power on
      machine MVA rating as a function of turbine flow.
    fp10: Flow P10 (Fp10).  Turbine Flow value for point 10 for lookup table representing per unit mechanical power on
      machine MVA rating as a function of turbine flow.
    pmss1: Pmss Flow P1 (Pmss1).  Mechanical Power output Pmss for Turbine Flow point 1 for lookup table representing
      per unit mechanical power on machine MVA rating as a function of turbine flow.
    pmss2: Pmss Flow P2 (Pmss2).  Mechanical Power output Pmss for Turbine Flow point 2 for lookup table representing
      per unit mechanical power on machine MVA rating as a function of turbine flow.
    pmss3: Pmss Flow P3 (Pmss3).  Mechanical Power output Pmss for Turbine Flow point 3 for lookup table representing
      per unit mechanical power on machine MVA rating as a function of turbine flow.
    pmss4: Pmss Flow P4 (Pmss4).  Mechanical Power output Pmss for Turbine Flow point 4 for lookup table representing
      per unit mechanical power on machine MVA rating as a function of turbine flow.
    pmss5: Pmss Flow P5 (Pmss5).  Mechanical Power output Pmss for Turbine Flow point 5 for lookup table representing
      per unit mechanical power on machine MVA rating as a function of turbine flow.
    pmss6: Pmss Flow P6 (Pmss6).  Mechanical Power output Pmss for Turbine Flow point 6 for lookup table representing
      per unit mechanical power on machine MVA rating as a function of turbine flow.
    pmss7: Pmss Flow P7 (Pmss7).  Mechanical Power output Pmss for Turbine Flow point 7 for lookup table representing
      per unit mechanical power on machine MVA rating as a function of turbine flow.
    pmss8: Pmss Flow P8 (Pmss8).  Mechanical Power output Pmss for Turbine Flow point 8 for lookup table representing
      per unit mechanical power on machine MVA rating as a function of turbine flow.
    pmss9: Pmss Flow P9 (Pmss9).  Mechanical Power output Pmss for Turbine Flow point 9 for lookup table representing
      per unit mechanical power on machine MVA rating as a function of turbine flow.
    pmss10: Pmss Flow P10 (Pmss10).  Mechanical Power output Pmss for Turbine Flow point 10 for lookup table
      representing per unit mechanical power on machine MVA rating as a function of turbine flow.
    """

    mwbase : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rpg : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rpp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tpe : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ki : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kd : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    td : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tp : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tdv : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tg : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    gtmxop : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    gtmxcl : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    gmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    gmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    dturb : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tw : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    db : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    dpv : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    dicn : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    feedbackSignal : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    gv1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    gv2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    gv3 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    gv4 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    gv5 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    fl1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    fl2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    fl3 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    fl4 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    fl5 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    fp1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    fp2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    fp3 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    fp4 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    fp5 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    fp6 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    fp7 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    fp8 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    fp9 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    fp10 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmss1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmss2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmss3 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmss4 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmss5 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmss6 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmss7 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmss8 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmss9 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmss10 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
