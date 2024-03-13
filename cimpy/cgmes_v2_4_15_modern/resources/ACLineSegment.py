"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .Conductor import Conductor

@dataclass
class ACLineSegment(Conductor):
    """
    A wire or combination of wires, with consistent electrical characteristics, building a single electrical system,
      used to carry alternating current between points in the power system. For symmetrical, transposed 3ph lines,
      it is sufficient to use  attributes of the line segment, which describe impedances and admittances for the
      entire length of the segment.  Additionally impedances can be computed by using length and associated per
      length impedances. The BaseVoltage at the two ends of ACLineSegments in a Line shall have the same
      BaseVoltage.nominalVoltage. However, boundary lines  may have slightly different BaseVoltage.nominalVoltages
      and  variation is allowed. Larger voltage difference in general requires use of an equivalent branch.

    b0ch: Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.
    bch: Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value
      represents the full charging over the full length of the line.
    g0ch: Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section.
    gch: Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section.
    r: Positive sequence series resistance of the entire line section.
    r0: Zero sequence series resistance of the entire line section.
    shortCircuitEndTemperature: Maximum permitted temperature at the end of SC for the calculation of minimum short-
      circuit currents. Used for short circuit data exchange according to IEC 60909
    x: Positive sequence series reactance of the entire line section.
    x0: Zero sequence series reactance of the entire line section.
    """

    b0ch : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    bch : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    g0ch : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    gch : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    r : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    r0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    shortCircuitEndTemperature : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    x : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    x0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
