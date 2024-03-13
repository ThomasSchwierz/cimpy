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
class GovCT1(TurbineGovernorDynamics):
    """
    General model for any prime mover with a PID governor, used primarily for combustion turbine and combined cycle
      units. This model can be used to represent a variety of prime movers controlled by PID governors.  It is
      suitable, for example, for representation of     Additional information on this model is available in the 2012
      IEEE report, , section 3.1.2.3 page 3-4 (GGOV1).

    mwbase: Base for power values (MWbase) (> 0).  Unit = MW.
    r: Permanent droop (R).  Typical Value = 0.04.
    rselect: Feedback signal for droop (Rselect).  Typical Value = electricalPower.
    tpelec: Electrical power transducer time constant (Tpelec) (>0).  Typical Value = 1.
    maxerr: Maximum value for speed error signal (maxerr).  Typical Value = 0.05.
    minerr: Minimum value for speed error signal (minerr).  Typical Value = -0.05.
    kpgov: Governor proportional gain (Kpgov).  Typical Value = 10.
    kigov: Governor integral gain (Kigov).  Typical Value = 2.
    kdgov: Governor derivative gain (Kdgov).  Typical Value = 0.
    tdgov: Governor derivative controller time constant (Tdgov).  Typical Value = 1.
    vmax: Maximum valve position limit (Vmax).  Typical Value = 1.
    vmin: Minimum valve position limit (Vmin).  Typical Value = 0.15.
    tact: Actuator time constant (Tact).  Typical Value = 0.5.
    kturb: Turbine gain (Kturb) (>0).  Typical Value = 1.5.
    wfnl: No load fuel flow (Wfnl).  Typical Value = 0.2.
    tb: Turbine lag time constant (Tb) (>0).  Typical Value = 0.5.
    tc: Turbine lead time constant (Tc).  Typical Value = 0.
    wfspd: Switch for fuel source characteristic to recognize that fuel flow, for a given fuel valve stroke, can be
      proportional to engine speed (Wfspd). true = fuel flow proportional to speed (for some gas turbines and
      diesel engines with positive displacement fuel injectors) false = fuel control system keeps fuel flow
      independent of engine speed. Typical Value = true.
    teng: Transport time delay for diesel engine used in representing diesel engines where there is a small but
      measurable transport delay between a change in fuel flow setting and the development of torque (Teng).
      Teng should be zero in all but special cases where this transport delay is of particular concern.
      Typical Value = 0.
    tfload: Load Limiter time constant (Tfload) (>0).  Typical Value = 3.
    kpload: Load limiter proportional gain for PI controller (Kpload).  Typical Value = 2.
    kiload: Load limiter integral gain for PI controller (Kiload).  Typical Value = 0.67.
    ldref: Load limiter reference value (Ldref).  Typical Value = 1.
    dm: Speed sensitivity coefficient (Dm).  Dm can represent either the variation of the engine power with the shaft
      speed or the variation of maximum power capability with shaft speed.  If it is positive it describes the
      falling slope of the engine speed verses power characteristic as speed increases. A slightly falling
      characteristic is typical for reciprocating engines and some aero-derivative turbines.  If it is negative
      the engine power is assumed to be unaffected by the shaft speed, but the maximum permissible fuel flow is
      taken to fall with falling shaft speed. This is characteristic of single-shaft industrial turbines due to
      exhaust temperature limits.  Typical Value = 0.
    ropen: Maximum valve opening rate (Ropen).  Unit = PU/sec.  Typical Value = 0.10.
    rclose: Minimum valve closing rate (Rclose).  Unit = PU/sec.  Typical Value = -0.1.
    kimw: Power controller (reset) gain (Kimw).  The default value of 0.01 corresponds to a reset time of 100 seconds.
      A value of 0.001 corresponds to a relatively slow acting load controller.  Typical Value = 0.01.
    aset: Acceleration limiter setpoint (Aset).  Unit = PU/sec.  Typical Value = 0.01.
    ka: Acceleration limiter gain (Ka).  Typical Value = 10.
    ta: Acceleration limiter time constant (Ta) (>0).  Typical Value = 0.1.
    db: Speed governor dead band in per unit speed (db).  In the majority of applications, it is recommended that this
      value be set to zero.  Typical Value = 0.
    tsa: Temperature detection lead time constant (Tsa).  Typical Value = 4.
    tsb: Temperature detection lag time constant (Tsb).  Typical Value = 5.
    rup: Maximum rate of load limit increase (Rup).  Typical Value = 99.
    rdown: Maximum rate of load limit decrease (Rdown).  Typical Value = -99.
    """

    mwbase : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    r : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rselect : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tpelec : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    maxerr : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    minerr : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kpgov : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kigov : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kdgov : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tdgov : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tact : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kturb : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    wfnl : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tb : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    wfspd : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    teng : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tfload : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kpload : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kiload : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ldref : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    dm : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ropen : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rclose : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kimw : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    aset : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ka : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    db : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tsa : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tsb : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rup : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rdown : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
