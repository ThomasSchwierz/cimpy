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
class MechanicalLoadDynamics(DynamicsFunctionBlock):
    """
    Mechanical load function block whose behavior is described by reference to a standard model

    SynchronousMachineDynamics: Synchronous machine model with which this mechanical load model is associated.
    AsynchronousMachineDynamics: Asynchronous machine model with which this mechanical load model is associated.
    """

    SynchronousMachineDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    AsynchronousMachineDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
