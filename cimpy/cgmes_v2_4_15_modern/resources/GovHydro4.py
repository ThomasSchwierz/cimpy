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
class GovHydro4(TurbineGovernorDynamics):
    """
    Hydro turbine and governor. Represents plants with straight-forward penstock configurations and hydraulic governors
      of traditional 'dashpot' type.  This model can be used to represent simple, Francis, Pelton or Kaplan
      turbines.

    mwbase: Base for power values (MWbase) (>0).  Unit = MW.
    tg: Gate servo time constant (Tg) (>0).  Typical Value = 0.5.
    tp: Pilot servo time constant (Tp).  Typical Value = 0.1.
    uo: Max gate opening velocity (Uo).  Typical Vlaue = 0.2.
    uc: Max gate closing velocity (Uc).  Typical Value = 0.2.
    gmax: Maximum gate opening, PU of MWbase (Gmax).  Typical Value = 1.
    gmin: Minimum gate opening, PU of MWbase (Gmin).  Typical Value = 0.
    rperm: Permanent droop (Rperm).  Typical Value = 0.05.
    rtemp: Temporary droop (Rtemp).  Typical Value = 0.3.
    tr: Dashpot time constant (Tr) (>0).  Typical Value = 5.
    tw: Water inertia time constant (Tw) (>0).  Typical Value = 1.
    at: Turbine gain (At).  Typical Value = 1.2.
    dturb: Turbine damping factor (Dturb).  Unit = delta P (PU of MWbase) / delta speed (PU). Typical Value = 0.5.
      Typical Value Francis = 1.1, Kaplan = 1.1.
    hdam: Head available at dam (hdam).  Typical Value = 1.
    qn1: No-load flow at nominal head (Qnl). Typical Value = 0.08.  Typical Value Francis = 0, Kaplan = 0.
    db1: Intentional deadband width (db1).  Unit = Hz.  Typical Value = 0.
    eps: Intentional db hysteresis (eps).  Unit = Hz.  Typical Value = 0.
    db2: Unintentional dead-band (db2).  Unit = MW.  Typical Value = 0.
    gv0: Nonlinear gain point 0, PU gv (Gv0). Typical Value = 0.  Typical Value Francis = 0.1, Kaplan = 0.1.
    pgv0: Nonlinear gain point 0, PU power (Pgv0).  Typical Value = 0.
    gv1: Nonlinear gain point 1, PU gv (Gv1). Typical Value = 0.  Typical Value Francis = 0.4, Kaplan = 0.4.
    pgv1: Nonlinear gain point 1, PU power (Pgv1). Typical Value = 0.  Typical Value Francis = 0.42, Kaplan = 0.35.
    gv2: Nonlinear gain point 2, PU gv (Gv2). Typical Value = 0.  Typical Value Francis = 0.5, Kaplan = 0.5.
    pgv2: Nonlinear gain point 2, PU power (Pgv2). Typical Value = 0.  Typical Value Francis = 0.56, Kaplan = 0.468.
    gv3: Nonlinear gain point 3, PU gv (Gv3). Typical Value = 0.  Typical Value Francis = 0.7, Kaplan = 0.7.
    pgv3: Nonlinear gain point 3, PU power (Pgv3). Typical Value = 0.  Typical Value Francis = 0.8, Kaplan = 0.796.
    gv4: Nonlinear gain point 4, PU gv (Gv4). Typical Value = 0.  Typical Value Francis = 0.8, Kaplan = 0.8.
    pgv4: Nonlinear gain point 4, PU power (Pgv4). Typical Value = 0.  Typical Value Francis = 0.9, Kaplan = 0.917.
    gv5: Nonlinear gain point 5, PU gv (Gv5). Typical Value = 0.  Typical Value Francis = 0.9, Kaplan = 0.9.
    pgv5: Nonlinear gain point 5, PU power (Pgv5).  Typical Value = 0.  Typical Value Francis = 0.97, Kaplan = 0.99.
    bgv0: Kaplan blade servo point 0 (Bgv0).  Typical Value = 0.
    bgv1: Kaplan blade servo point 1 (Bgv1).  Typical Value = 0.
    bgv2: Kaplan blade servo point 2 (Bgv2). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.1.
    bgv3: Kaplan blade servo point 3 (Bgv3). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.667.
    bgv4: Kaplan blade servo point 4 (Bgv4).  Typical Value = 0.  Typical Value Francis = 0, Kaplan = 0.9.
    bgv5: Kaplan blade servo point 5 (Bgv5). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 1.
    bmax: Maximum blade adjustment factor (Bmax). Typical Value = 0.  Typical Value Francis = 0, Kaplan = 1.1276.
    tblade: Blade servo time constant (Tblade).  Typical Value = 100.
    """

    mwbase : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tg : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tp : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    uo : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    uc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    gmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    gmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rperm : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rtemp : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tr : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tw : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    at : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    dturb : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    hdam : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    qn1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    db1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    eps : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    db2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    gv0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pgv0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

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

    bgv0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    bgv1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    bgv2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    bgv3 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    bgv4 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    bgv5 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    bmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tblade : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
