"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .PowerSystemResource import PowerSystemResource

@dataclass
class TapChanger(PowerSystemResource):
    """
    Mechanism for changing transformer winding tap positions.

    highStep: Highest possible tap step position, advance from neutral. The attribute shall be greater than lowStep.
    lowStep: Lowest possible tap step position, retard from neutral
    ltcFlag: Specifies whether or not a TapChanger has load tap changing capabilities.
    neutralStep: The neutral tap step position for this winding. The attribute shall be equal or greater than lowStep
      and equal or less than highStep.
    neutralU: Voltage at which the winding operates at the neutral tap setting.
    normalStep: The tap step position used in `normal` network operation for this winding. For a `Fixed` tap changer
      indicates the current physical tap setting. The attribute shall be equal or greater than lowStep
      and equal or less than highStep.
    TapChangerControl: The tap changers that participates in this regulating tap control scheme.
    TapSchedules: A TapSchedule is associated with a TapChanger.
    SvTapStep: The tap step state associated with the tap changer.
    controlEnabled: Specifies the regulation status of the equipment.  True is regulating, false is not regulating.
    step: Tap changer position. Starting step for a steady state solution. Non integer values are allowed to support
      continuous tap variables. The reasons for continuous value are to support study cases where no discrete
      tap changers has yet been designed, a solutions where a narrow voltage band force the tap step to
      oscillate or accommodate for a continuous solution as input. The attribute shall be equal or greater
      than lowStep and equal or less than highStep.
    """

    highStep : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    lowStep : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    ltcFlag : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    neutralStep : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    neutralU : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    normalStep : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    TapChangerControl : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    # *Association not used*
    # Type M:0..n in CIM
    # TapSchedules : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM
    # SvTapStep : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.SV, ]}) # noqa: E501

    controlEnabled : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    step : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ, Profile.SV, Profile.SSH,  }
