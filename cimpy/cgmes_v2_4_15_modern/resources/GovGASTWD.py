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
class GovGASTWD(TurbineGovernorDynamics):
    """
    Woodward Gas turbine governor model.

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    kdroop: (Kdroop).
    kp: PID Proportional gain (Kp).
    ki: Isochronous Governor Gain (Ki).
    kd: Drop Governor Gain (Kd).
    etd: Turbine and exhaust delay (Etd).
    tcd: Compressor discharge time constant (Tcd).
    trate: Turbine rating (Trate).  Unit = MW.
    t: Fuel Control Time Constant (T).
    tmax: Maximum Turbine limit (Tmax).
    tmin: Minimum Turbine limit (Tmin).
    ecr: Combustion reaction time delay (Ecr).
    k3: Ratio of Fuel Adjustment (K3).
    a: Valve positioner ().
    b: Valve positioner ().
    c: Valve positioner ().
    tf: Fuel system time constant (Tf).
    kf: Fuel system feedback (Kf).
    k5: Gain of radiation shield (K5).
    k4: Gain of radiation shield (K4).
    t3: Radiation shield time constant (T3).
    t4: Thermocouple time constant (T4).
    tt: Temperature controller integration rate (Tt).
    t5: Temperature control time constant (T5).
    af1: Exhaust temperature Parameter (Af1).
    bf1: (Bf1).  Bf1 = E(1-w) where E (speed sensitivity coefficient) is 0.55 to 0.65 x Tr.
    af2: Coefficient equal to 0.5(1-speed) (Af2).
    bf2: Turbine Torque Coefficient K (depends on heating value of fuel stream in combustion chamber) (Bf2).
    cf2: Coefficient defining fuel flow where power output is 0% (Cf2).  Synchronous but no output.  Typically 0.23 x
      K(23% fuel flow).
    tr: Rated temperature (Tr).
    k6: Minimum fuel flow (K6).
    tc: Temperature control (Tc).
    td: Power transducer time constant (Td).
    """

    mwbase : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kdroop : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ki : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kd : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    etd : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tcd : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    trate : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ecr : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k3 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    a : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    b : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    c : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tf : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kf : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k5 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k4 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t4 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tt : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t5 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    af1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    bf1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    af2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    bf2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    cf2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tr : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    k6 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    td : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
