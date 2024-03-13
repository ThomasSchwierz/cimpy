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
class PFVArControllerType1Dynamics(DynamicsFunctionBlock):
    """
    Power Factor or VAr controller Type I function block whose behaviour is described by reference to a standard model

    RemoteInputSignal: Remote input signal used by this Power Factor or VAr controller Type I model.
    ExcitationSystemDynamics: Excitation system model with which this Power Factor or VAr controller Type I model is
      associated.
    VoltageAdjusterDynamics: Voltage adjuster model associated with this Power Factor or VA controller Type I model.
    """

    # *Association not used*
    # Type M:0..1 in CIM
    # RemoteInputSignal : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    ExcitationSystemDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    # *Association not used*
    # Type M:0..1 in CIM
    # VoltageAdjusterDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
