"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .DynamicsFunctionBlock import DynamicsFunctionBlock

@dataclass
class TurbineGovernorDynamics(DynamicsFunctionBlock):
    """
    Turbine-governor function block whose behavior is described by reference to a standard model

    SynchronousMachineDynamics: Turbine-governor model associated with this synchronous machine model.
    AsynchronousMachineDynamics: Asynchronous machine model with which this turbine-governor model is associated.
    TurbineLoadControllerDynamics: Turbine load controller providing input to this turbine-governor.
    """

    SynchronousMachineDynamics : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    AsynchronousMachineDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    # *Association not used*
    # Type M:0..1 in CIM
    # TurbineLoadControllerDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
