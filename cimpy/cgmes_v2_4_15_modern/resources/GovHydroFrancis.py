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
class GovHydroFrancis(TurbineGovernorDynamics):
    """
    Detailed hydro unit - Francis model.  This model can be used to represent three types of governors. A schematic of
      the hydraulic system of detailed hydro unit models, like Francis and Pelton, is provided in the
      DetailedHydroModelHydraulicSystem diagram.

    am: Opening section S at the maximum efficiency (Am).  Typical Value = 0.7.
    av0: Area of the surge tank (A). Unit = m. Typical Value = 30.
    av1: Area of the compensation tank (A). Unit = m. Typical Value = 700.
    bp: Droop (Bp).  Typical Value = 0.05.
    db1: Intentional dead-band width (DB1).  Unit = Hz.  Typical Value = 0.
    etamax: Maximum efficiency (EtaMax).  Typical Value = 1.05.
    governorControl: Governor control flag (Cflag).  Typical Value = mechanicHydrolicTachoAccelerator.
    h1: Head of compensation chamber water level with respect to the level of penstock (H).  Unit = m. Typical Value =
      4.
    h2: Head of surge tank water level with respect to the level of penstock (H).  Unit = m. Typical Value = 40.
    hn: Rated hydraulic head (H).  Unit = m. Typical Value = 250.
    kc: Penstock loss coefficient (due to friction) (Kc).  Typical Value = 0.025.
    kg: Water tunnel and surge chamber loss coefficient (due to friction) (Kg).  Typical Value = 0.025.
    kt: Washout gain (Kt).  Typical Value = 0.25.
    qc0: No-load turbine flow at nominal head (Qc0).  Typical Value = 0.21.
    qn: Rated flow (Q). Unit = m/s. Typical Value = 40.
    ta: Derivative gain (Ta).  Typical Value = 3.
    td: Washout time constant (Td).  Typical Value = 3.
    ts: Gate servo time constant (Ts).  Typical Value = 0.5.
    twnc: Water inertia time constant (Twnc).  Typical Value = 1.
    twng: Water tunnel and surge chamber inertia time constant (Twng). Typical Value = 3.
    tx: Derivative feedback gain (Tx).  Typical Value = 1.
    va: Maximum gate opening velocity (Va).  Unit = PU/sec.  Typical Value = 0.011.
    valvmax: Maximum gate opening (ValvMax).  Typical Value = 1.
    valvmin: Minimum gate opening (ValvMin).  Typical Value = 0.
    vc: Maximum gate closing velocity (Vc).  Unit = PU/sec.  Typical Value = -0.011.
    waterTunnelSurgeChamberSimulation: Water tunnel and surge chamber simulation (Tflag). true = enable of water tunnel
      and surge chamber simulation false = inhibit of water tunnel and surge
      chamber simulation. Typical Value = false.
    zsfc: Head of upper water level with respect to the level of penstock (Zsfc).  Unit = m.  Typical Value = 25.
    """

    am : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    av0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    av1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    bp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    db1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    etamax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    governorControl : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    h1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    h2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    hn : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kg : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kt : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    qc0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    qn : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    td : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ts : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    twnc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    twng : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tx : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    va : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    valvmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    valvmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    waterTunnelSurgeChamberSimulation : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    zsfc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
