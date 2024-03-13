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
class Control(IdentifiedObject):
    """
    Control is used for supervisory/device control. It represents control outputs that are used to change the state in a
      process, e.g. close or open breaker, a set point value or a raise lower command.

    controlType: Specifies the type of Control, e.g. BreakerOn/Off, GeneratorVoltageSetPoint, TieLineFlow etc. The
      ControlType.name shall be unique among all specified types and describe the type.
    operationInProgress: Indicates that a client is currently sending control commands that has not completed.
    timeStamp: The last time a control output was sent.
    unitMultiplier: The unit multiplier of the controlled quantity.
    unitSymbol: The unit of measure of the controlled quantity.
    PowerSystemResource: The controller outputs used to actually govern a regulating device, e.g. the magnetization of a
      synchronous machine or capacitor bank breaker actuator.
    """

    controlType : str = Field(default="", json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    operationInProgress : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    timeStamp : str = Field(default="", json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    unitMultiplier : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    unitSymbol : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    PowerSystemResource : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
