"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .TapChanger import TapChanger

@dataclass
class RatioTapChanger(TapChanger):
    """
    A tap changer that changes the voltage ratio impacting the voltage magnitude but not the phase angle across the
      transformer.

    tculControlMode: Specifies the regulation control mode (voltage or reactive) of the RatioTapChanger.
    stepVoltageIncrement: Tap step increment, in per cent of nominal voltage, per step position.
    RatioTapChangerTable: The ratio tap changer of this tap ratio table.
    TransformerEnd: Ratio tap changer associated with this transformer end.
    """

    tculControlMode : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    stepVoltageIncrement : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    RatioTapChangerTable : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    TransformerEnd : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ, Profile.SSH,  }
