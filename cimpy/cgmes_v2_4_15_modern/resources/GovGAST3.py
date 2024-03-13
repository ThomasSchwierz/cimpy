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
class GovGAST3(TurbineGovernorDynamics):
    """
    Generic turbogas with acceleration and temperature controller.

    bp: Droop (bp).  Typical Value = 0.05.
    tg: Time constant of speed governor (Tg).  Typical Value = 0.05.
    rcmx: Maximum fuel flow (RCMX).  Typical Value = 1.
    rcmn: Minimum fuel flow (RCMN).  Typical Value = -0.1.
    ky: Coefficient of transfer function of fuel valve positioner (Ky).  Typical Value = 1.
    ty: Time constant of fuel valve positioner (Ty).  Typical Value = 0.2.
    tac: Fuel control time constant (Tac).  Typical Value = 0.1.
    kac: Fuel system feedback (K).  Typical Value = 0.
    tc: Compressor discharge volume time constant (Tc).  Typical Value = 0.2.
    bca: Acceleration limit set-point (Bca).  Unit = 1/s.  Typical Value = 0.01.
    kca: Acceleration control integral gain (Kca). Unit = 1/s.  Typical Value = 100.
    dtc: Exhaust temperature variation due to fuel flow increasing from 0 to 1 PU (deltaTc).  Typical Value = 390.
    ka: Minimum fuel flow (Ka).  Typical Value = 0.23.
    tsi: Time constant of radiation shield (Tsi).  Typical Value = 15.
    ksi: Gain of radiation shield (Ksi).  Typical Value = 0.8.
    ttc: Time constant of thermocouple (Ttc).  Typical Value = 2.5.
    tfen: Turbine rated exhaust temperature correspondent to Pm=1 PU (Tfen).  Typical Value = 540.
    td: Temperature controller derivative gain (Td).  Typical Value = 3.3.
    tt: Temperature controller integration rate (Tt).  Typical Value = 250.
    mxef: Fuel flow maximum positive error value (MX).  Typical Value = 0.05.
    mnef: Fuel flow maximum negative error value (MN).  Typical Value = -0.05.
    """

    bp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tg : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rcmx : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rcmn : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ky : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ty : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tac : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kac : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    bca : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kca : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    dtc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ka : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tsi : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ksi : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ttc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tfen : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    td : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tt : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    mxef : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    mnef : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
