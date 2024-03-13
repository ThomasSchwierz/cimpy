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
class GovHydroIEEE2(TurbineGovernorDynamics):
    """
    IEEE hydro turbine governor model represents plants with straightforward penstock configurations and hydraulic-
      dashpot governors.  Ref

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    tg: Gate servo time constant (Tg).  Typical Value = 0.5.
    tp: Pilot servo valve time constant (Tp).  Typical Value = 0.03.
    uo: Maximum gate opening velocity (Uo). Unit = PU/sec.  Typical Value = 0.1.
    uc: Maximum gate closing velocity (Uc) (<0).  Typical Value = -0.1.
    pmax: Maximum gate opening (Pmax).  Typical Value = 1.
    pmin: Minimum gate opening (Pmin).  Typical Value = 0.
    rperm: Permanent droop (Rperm).  Typical Value = 0.05.
    rtemp: Temporary droop (Rtemp).  Typical Value = 0.5.
    tr: Dashpot time constant (Tr).  Typical Value = 12.
    tw: Water inertia time constant (Tw).  Typical Value = 2.
    kturb: Turbine gain (Kturb).  Typical Value = 1.
    aturb: Turbine numerator multiplier (Aturb).  Typical Value = -1.
    bturb: Turbine denominator multiplier (Bturb).  Typical Value = 0.5.
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

    tg : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tp : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    uo : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    uc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rperm : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rtemp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tr : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tw : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kturb : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    aturb : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    bturb : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

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
