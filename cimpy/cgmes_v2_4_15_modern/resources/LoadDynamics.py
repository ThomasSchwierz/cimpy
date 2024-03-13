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
class LoadDynamics(IdentifiedObject):
    """
    Load whose behaviour is described by reference to a standard model   A standard feature of dynamic load behaviour
      modelling is the ability to associate the same behaviour to multiple energy consumers by means of a single
      aggregate load definition.  Aggregate loads are used to represent all or part of the real and reactive load
      from one or more loads in the static (power flow) data. This load is usually the aggregation of many
      individual load devices and the load model is approximate representation of the aggregate response of the load
      devices to system disturbances. The load model is always applied to individual bus loads (energy consumers)
      but a single set of load model parameters can used for all loads in the grouping.

    EnergyConsumer: Energy consumer to which this dynamics load model applies.
    """

    # *Association not used*
    # Type M:0..n in CIM
    # EnergyConsumer : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
