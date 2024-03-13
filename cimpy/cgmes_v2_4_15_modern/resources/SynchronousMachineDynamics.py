"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .RotatingMachineDynamics import RotatingMachineDynamics

@dataclass
class SynchronousMachineDynamics(RotatingMachineDynamics):
    """
    Synchronous machine whose behaviour is described by reference to a standard model expressed in one of the following
      forms:

    SynchronousMachine: Synchronous machine to which synchronous machine dynamics model applies.
    TurbineGovernorDynamics: Synchronous machine model with which this turbine-governor model is associated.
    ExcitationSystemDynamics: Excitation system model associated with this synchronous machine model.
    MechanicalLoadDynamics: Mechanical load model associated with this synchronous machine model.
    GenICompensationForGenJ: Compensation of voltage compensator`s generator for current flow out of this  generator.
    """

    SynchronousMachine : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    # *Association not used*
    # Type M:0..n in CIM
    # TurbineGovernorDynamics : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM
    # ExcitationSystemDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM
    # MechanicalLoadDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..n in CIM
    # GenICompensationForGenJ : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
