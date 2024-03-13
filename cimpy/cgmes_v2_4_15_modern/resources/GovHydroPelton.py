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
class GovHydroPelton(TurbineGovernorDynamics):
    """
    Detailed hydro unit - Pelton model.  This model can be used to represent the dynamic related to water tunnel and
      surge chamber. A schematic of the hydraulic system of detailed hydro unit models, like Francis and Pelton, is
      located under the GovHydroFrancis class.

    av0: Area of the surge tank (A). Unit = m. Typical Value = 30.
    av1: Area of the compensation tank (A). Unit = m. Typical Value = 700.
    bp: Droop (bp).  Typical Value = 0.05.
    db1: Intentional dead-band width (DB1).  Unit = Hz.  Typical Value = 0.
    db2: Intentional dead-band width of valve opening error (DB2). Unit = Hz.  Typical Value = 0.01.
    h1: Head of compensation chamber water level with respect to the level of penstock (H).  Unit = m. Typical Value =
      4.
    h2: Head of surge tank water level with respect to the level of penstock (H).  Unit = m. Typical Value = 40.
    hn: Rated hydraulic head (H).  Unit = m. Typical Value = 250.
    kc: Penstock loss coefficient (due to friction) (Kc).  Typical Value = 0.025.
    kg: Water tunnel and surge chamber loss coefficient (due to friction) (Kg).  Typical Value = -0.025.
    qc0: No-load turbine flow at nominal head (Qc0).  Typical Value = 0.05.
    qn: Rated flow (Q). Unit = m/s. Typical Value = 40.
    simplifiedPelton: Simplified Pelton model simulation (Sflag). true = enable of simplified Pelton model simulation
      false = enable of complete Pelton model simulation (non linear gain). Typical Value = false.
    staticCompensating: Static compensating characteristic (Cflag). true = enable of static compensating characteristic
      false = inhibit of static compensating characteristic. Typical Value = false.
    ta: Derivative gain (accelerometer time constant) (Ta).  Typical Value = 3.
    ts: Gate servo time constant (Ts).  Typical Value = 0.15.
    tv: Servomotor integrator time constant (TV).  Typical Value = 0.3.
    twnc: Water inertia time constant (Twnc).  Typical Value = 1.
    twng: Water tunnel and surge chamber inertia time constant (Twng). Typical Value = 3.
    tx: Electronic integrator time constant (Tx).  Typical Value = 0.5.
    va: Maximum gate opening velocity (Va).  Unit = PU/sec.  Typical Value = 0.016.
    valvmax: Maximum gate opening (ValvMax).  Typical Value = 1.
    valvmin: Minimum gate opening (ValvMin).  Typical Value = 0.
    vav: Maximum servomotor valve opening velocity (Vav).  Typical Value = 0.017.
    vc: Maximum gate closing velocity (Vc).  Unit = PU/sec.  Typical Value = -0.016.
    vcv: Maximum servomotor valve closing velocity (Vcv).  Typical Value = -0.017.
    waterTunnelSurgeChamberSimulation: Water tunnel and surge chamber simulation (Tflag). true = enable of water tunnel
      and surge chamber simulation false = inhibit of water tunnel and surge
      chamber simulation. Typical Value = false.
    zsfc: Head of upper water level with respect to the level of penstock (Zsfc).  Unit = m. Typical Value = 25.
    """

    av0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    av1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    bp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    db1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    db2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    h1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    h2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    hn : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kg : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    qc0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    qn : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    simplifiedPelton : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    staticCompensating : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ts : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tv : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    twnc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    twng : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tx : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    va : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    valvmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    valvmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vav : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vcv : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    waterTunnelSurgeChamberSimulation : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    zsfc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
