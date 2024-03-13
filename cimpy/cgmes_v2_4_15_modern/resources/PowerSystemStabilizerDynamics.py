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
class PowerSystemStabilizerDynamics(DynamicsFunctionBlock):
    """
    Power system stabilizer function block whose behaviour is described by reference to a standard model

    RemoteInputSignal: Remote input signal used by this power system stabilizer model.
    ExcitationSystemDynamics: Excitation system model with which this power system stabilizer model is associated.
    """

    # *Association not used*
    # Type M:0..n in CIM
    # RemoteInputSignal : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    ExcitationSystemDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
