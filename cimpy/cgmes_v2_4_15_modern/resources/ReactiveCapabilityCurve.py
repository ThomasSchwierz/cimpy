"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .Curve import Curve

@dataclass
class ReactiveCapabilityCurve(Curve):
    """
    Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring
      modes. For each active power value there is a corresponding high and low reactive power limit  value.
      Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis
      values represent reactive minimum and the Y2 axis values represent reactive maximum.

    EquivalentInjection: The reactive capability curve used by this equivalent injection.
    InitiallyUsedBySynchronousMachines: The default reactive capability curve for use by a synchronous machine.
    """

    # *Association not used*
    # Type M:0..n in CIM
    # EquivalentInjection : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    # *Association not used*
    # Type M:1..n in CIM
    # InitiallyUsedBySynchronousMachines : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
