"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .IdentifiedObject import IdentifiedObject

@dataclass
class WindContPType3IEC(IdentifiedObject):
    """
    P control model Type 3.  Reference: IEC Standard 61400-27-1 Section 6.6.5.3.

    dpmax: Maximum wind turbine power ramp rate (). It is project dependent parameter.
    dtrisemaxlvrt: Limitation of torque rise rate during LVRT for S (d). It is project dependent parameter.
    kdtd: Gain for active drive train damping (). It is type dependent parameter.
    kip: PI controller integration parameter (). It is type dependent parameter.
    kpp: PI controller proportional gain (). It is type dependent parameter.
    mplvrt: Enable LVRT power control mode (M true = 1: voltage control false = 0: reactive power control.  It is
      project dependent parameter.
    omegaoffset: Offset to reference value that limits controller action during rotor speed changes (omega). It is case
      dependent parameter.
    pdtdmax: Maximum active drive train damping power (). It is type dependent parameter.
    rramp: Ramp limitation of torque, required in some grid codes (). It is project dependent parameter.
    tdvs: Timedelay after deep voltage sags (T). It is project dependent parameter.
    temin: Minimum electrical generator torque (). It is type dependent parameter.
    tomegafilt: Filter time constant for generator speed measurement (). It is type dependent parameter.
    tpfilt: Filter time constant for power measurement (). It is type dependent parameter.
    tpord: Time constant in power order lag (). It is type dependent parameter.
    tufilt: Filter time constant for voltage measurement (). It is type dependent parameter.
    tuscale: Voltage scaling factor of reset-torque (T). It is project dependent parameter.
    twref: Time constant in speed reference filter (). It is type dependent parameter.
    udvs: Voltage limit for hold LVRT status after deep voltage sags (). It is project dependent parameter.
    updip: Voltage dip threshold for P-control ().  Part of turbine control, often different (e.g 0.8) from converter
      thresholds. It is project dependent parameter.
    wdtd: Active drive train damping frequency (omega). It can be calculated from two mass model parameters. It is type
      dependent parameter.
    zeta: Coefficient for active drive train damping (zeta). It is type dependent parameter.
    WindGenTurbineType3IEC: Wind turbine type 3 model with which this Wind control P type 3 model is associated.
    WindDynamicsLookupTable: The P control type 3 model with which this wind dynamics lookup table is associated.
    """

    dpmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    dtrisemaxlvrt : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kdtd : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kip : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kpp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    mplvrt : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    omegaoffset : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pdtdmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rramp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tdvs : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    temin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tomegafilt : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tpfilt : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tpord : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tufilt : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tuscale : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    twref : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    udvs : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    updip : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    wdtd : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    zeta : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    # *Association not used*
    # Type M:1 in CIM
    # WindGenTurbineType3IEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    # *Association not used*
    # Type M:2..n in CIM
    # WindDynamicsLookupTable : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
