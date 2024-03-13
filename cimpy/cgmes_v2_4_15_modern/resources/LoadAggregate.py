"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .LoadDynamics import LoadDynamics

@dataclass
class LoadAggregate(LoadDynamics):
    """
    Standard aggregate load model comprised of static and/or dynamic components.  A static load model represents the
      sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus
      voltage. A dynamic load model can used to represent the aggregate response of the motor components of the
      load.

    LoadStatic: Aggregate static load associated with this aggregate load.
    LoadMotor: Aggregate motor (dynamic) load associated with this aggregate load.
    """

    # *Association not used*
    # Type M:0..1 in CIM
    # LoadStatic : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM
    # LoadMotor : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
