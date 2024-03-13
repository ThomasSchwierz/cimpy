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
class WindContQIEC(IdentifiedObject):
    """
    Q control model.  Reference: IEC Standard 61400-27-1 Section 6.6.5.6.

    iqh1: Maximum reactive current injection during dip (i). It is type dependent parameter.
    iqmax: Maximum reactive current injection (i). It is type dependent parameter.
    iqmin: Minimum reactive current injection (i). It is type dependent parameter.
    iqpost: Post fault reactive current injection (). It is project dependent parameter.
    kiq: Reactive power PI controller integration gain (). It is type dependent parameter.
    kiu: Voltage PI controller integration gain (). It is type dependent parameter.
    kpq: Reactive power PI controller proportional gain (). It is type dependent parameter.
    kpu: Voltage PI controller proportional gain (). It is type dependent parameter.
    kqv: Voltage scaling factor for LVRT current (). It is project dependent parameter.
    qmax: Maximum reactive power (q). It is type dependent parameter.
    qmin: Minimum reactive power (q). It is type dependent parameter.
    rdroop: Resistive component of voltage drop impedance (). It is project dependent parameter.
    tiq: Time constant in reactive current lag (T). It is type dependent parameter.
    tpfilt: Power measurement filter time constant (). It is type dependent parameter.
    tpost: Length of time period where post fault reactive power is injected (). It is project dependent parameter.
    tqord: Time constant in reactive power order lag (). It is type dependent parameter.
    tufilt: Voltage measurement filter time constant (). It is type dependent parameter.
    udb1: Voltage dead band lower limit (). It is type dependent parameter.
    udb2: Voltage dead band upper limit (). It is type dependent parameter.
    umax: Maximum voltage in voltage PI controller integral term (u). It is type dependent parameter.
    umin: Minimum voltage in voltage PI controller integral term (u). It is type dependent parameter.
    uqdip: Voltage threshold for LVRT detection in q control (). It is type dependent parameter.
    uref0: User defined bias in voltage reference (), used when  =. It is case dependent parameter.
    windLVRTQcontrolModesType: Types of LVRT Q control modes (). It is project dependent parameter.
    windQcontrolModesType: Types of general wind turbine Q control modes ().  It is project dependent parameter.
    xdroop: Inductive component of voltage drop impedance (). It is project dependent parameter.
    WindTurbineType3or4IEC: Wind turbine type 3 or 4 model with which this reactive control mode is associated.
    """

    iqh1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    iqmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    iqmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    iqpost : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kiq : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kiu : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kpq : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kpu : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kqv : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    qmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    qmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rdroop : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tiq : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tpfilt : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tpost : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tqord : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tufilt : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    udb1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    udb2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    umax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    umin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    uqdip : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    uref0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    windLVRTQcontrolModesType : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    windQcontrolModesType : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    xdroop : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    # *Association not used*
    # Type M:1 in CIM
    # WindTurbineType3or4IEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
