"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .RegulatingCondEq import RegulatingCondEq

@dataclass
class ShuntCompensator(RegulatingCondEq):
    """
    A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is
      an individual capacitor or reactor.  A negative value for reactivePerSection indicates that the compensator is
      a reactor. ShuntCompensator is a single terminal device.  Ground is implied.

    aVRDelay: Time delay required for the device to be connected or disconnected by automatic voltage regulation (AVR).
    grounded: Used for Yn and Zn connections. True if the neutral is solidly grounded.
    maximumSections: The maximum number of sections that may be switched in.
    nomU: The voltage at which the nominal reactive power may be calculated. This should normally be within 10% of the
      voltage at which the capacitor is connected to the network.
    normalSections: The normal number of sections switched in.
    switchOnCount: The switch on count since the capacitor count was last reset or initialized.
    switchOnDate: The date and time when the capacitor bank was last switched on.
    voltageSensitivity: Voltage sensitivity required for the device to regulate the bus voltage, in voltage/reactive
      power.
    SvShuntCompensatorSections: The state for the number of shunt compensator sections in service.
    sections: Shunt compensator sections in use. Starting value for steady state solution. Non integer values are
      allowed to support continuous variables. The reasons for continuous value are to support study cases
      where no discrete shunt compensators has yet been designed, a solutions where a narrow voltage band
      force the sections to oscillate or accommodate for a continuous solution as input.
    """

    aVRDelay : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    grounded : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    maximumSections : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    nomU : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    normalSections : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    switchOnCount : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    switchOnDate : str = Field(default="", json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    voltageSensitivity : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    # *Association not used*
    # Type M:0..1 in CIM
    # SvShuntCompensatorSections : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.SV, ]}) # noqa: E501

    sections : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ, Profile.SV, Profile.SSH,  }
