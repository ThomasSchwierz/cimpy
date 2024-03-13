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
class WindContPitchAngleIEC(IdentifiedObject):
    """
    Pitch angle control model.  Reference: IEC Standard 61400-27-1 Section 6.6.5.8.

    dthetamax: Maximum pitch positive ramp rate (d). It is type dependent parameter. Unit = degrees/sec.
    dthetamin: Maximum pitch negative ramp rate (d). It is type dependent parameter. Unit = degrees/sec.
    kic: Power PI controller integration gain (). It is type dependent parameter.
    kiomega: Speed PI controller integration gain (). It is type dependent parameter.
    kpc: Power PI controller proportional gain (). It is type dependent parameter.
    kpomega: Speed PI controller proportional gain (). It is type dependent parameter.
    kpx: Pitch cross coupling gain (K). It is type dependent parameter.
    thetamax: Maximum pitch angle (). It is type dependent parameter.
    thetamin: Minimum pitch angle (). It is type dependent parameter.
    ttheta: Pitch time constant (t). It is type dependent parameter.
    WindGenTurbineType3IEC: Wind turbine type 3 model with which this pitch control model is associated.
    """

    dthetamax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    dthetamin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kic : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kiomega : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kpc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kpomega : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kpx : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    thetamax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    thetamin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ttheta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    # *Association not used*
    # Type M:1 in CIM
    # WindGenTurbineType3IEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
