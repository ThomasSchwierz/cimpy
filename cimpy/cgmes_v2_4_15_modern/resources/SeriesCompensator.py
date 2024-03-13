"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .ConductingEquipment import ConductingEquipment

@dataclass
class SeriesCompensator(ConductingEquipment):
    """
    A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.  It
      is a two terminal device.

    r: Positive sequence resistance.
    r0: Zero sequence resistance.
    x: Positive sequence reactance.
    x0: Zero sequence reactance.
    varistorPresent: Describe if a metal oxide varistor (mov) for over voltage protection is configured at the series
      compensator.
    varistorRatedCurrent: The maximum current the varistor is designed to handle at specified duration.
    varistorVoltageThreshold: The dc voltage at which the varistor start conducting.
    """

    r : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    r0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    x : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    x0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    varistorPresent : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    varistorRatedCurrent : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    varistorVoltageThreshold : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
