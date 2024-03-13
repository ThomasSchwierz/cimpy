"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .TurbineLoadControllerDynamics import TurbineLoadControllerDynamics

@dataclass
class TurbLCFB1(TurbineLoadControllerDynamics):
    """
    Turbine Load Controller model developed in the WECC.  This model represents a supervisory turbine load controller
      that acts to maintain turbine power at a set value by continuous adjustment of the turbine governor speed-load
      reference. This model is intended to represent slow reset 'outer loop' controllers managing the action of the
      turbine governor.

    mwbase: Base for power values (MWbase) (>0).  Unit = MW.
    speedReferenceGovernor: Type of turbine governor reference (Type). true = speed reference governor false = load
      reference governor. Typical Value = true.
    db: Controller dead band (db).  Typical Value = 0.
    emax: Maximum control error (Emax) (note 4).  Typical Value = 0.02.
    fb: Frequency bias gain (Fb).  Typical Value = 0.
    kp: Proportional gain (Kp).  Typical Value = 0.
    ki: Integral gain (Ki).  Typical Value = 0.
    fbf: Frequency bias flag (Fbf). true = enable frequency bias false = disable frequency bias. Typical Value = false.
    pbf: Power controller flag (Pbf). true = enable load controller false = disable load controller. Typical Value =
      false.
    tpelec: Power transducer time constant (Tpelec).  Typical Value = 0.
    irmax: Maximum turbine speed/load reference bias (Irmax) (note 3).  Typical Value = 0.
    pmwset: Power controller setpoint (Pmwset) (note 1).  Unit = MW. Typical Value = 0.
    """

    mwbase : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    speedReferenceGovernor : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    db : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    emax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    fb : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ki : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    fbf : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pbf : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tpelec : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    irmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pmwset : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
