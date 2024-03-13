"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcELIN1(ExcitationSystemDynamics):
    """
    Static PI transformer fed excitation system: ELIN (VATECH) - simplified model.  This model represents an all-static
      excitation system. A PI voltage controller establishes a desired field current set point for a proportional
      current controller. The integrator of the PI controller has a follow-up input to match its signal to the
      present field current.  A power system stabilizer with power input is included in the model.

    tfi: Current transducer time constant (Tfi).  Typical Value = 0.
    tnu: Controller reset time constant (Tnu).  Typical Value = 2.
    vpu: Voltage controller proportional gain (Vpu).  Typical Value = 34.5.
    vpi: Current controller gain (Vpi).  Typical Value = 12.45.
    vpnf: Controller follow up gain (Vpnf).  Typical Value = 2.
    dpnf: Controller follow up dead band (Dpnf).  Typical Value = 0.
    tsw: Stabilizer parameters (Tsw).  Typical Value = 3.
    efmin: Minimum open circuit excitation voltage (Efmin).  Typical Value = -5.
    efmax: Maximum open circuit excitation voltage (Efmax).  Typical Value = 5.
    xe: Excitation transformer effective reactance (Xe) (>=0).  Xe represents the regulation of the
      transformer/rectifier unit.  Typical Value = 0.06.
    ks1: Stabilizer Gain 1 (Ks1).  Typical Value = 0.
    ks2: Stabilizer Gain 2 (Ks2).  Typical Value = 0.
    ts1: Stabilizer Phase Lag Time Constant (Ts1).  Typical Value = 1.
    ts2: Stabilizer Filter Time Constant (Ts2).  Typical Value = 1.
    smax: Stabilizer Limit Output (smax).  Typical Value = 0.1.
    """

    tfi : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tnu : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vpu : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vpi : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vpnf : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    dpnf : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tsw : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    xe : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ks1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ks2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ts1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ts2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    smax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
