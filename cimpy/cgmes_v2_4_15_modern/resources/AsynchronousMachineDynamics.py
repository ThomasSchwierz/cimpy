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
class AsynchronousMachineDynamics(RotatingMachineDynamics):
    """
    Asynchronous machine whose behaviour is described by reference to a standard model expressed in either time constant
      reactance form or equivalent circuit form

    AsynchronousMachine: Asynchronous machine to which this asynchronous machine dynamics model applies.
    MechanicalLoadDynamics: Mechanical load model associated with this asynchronous machine model.
    WindTurbineType1or2Dynamics: Wind generator type 1 or 2 model associated with this asynchronous machine model.
    TurbineGovernorDynamics: Turbine-governor model associated with this asynchronous machine model.
    """

    AsynchronousMachine : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    # *Association not used*
    # Type M:0..1 in CIM
    # MechanicalLoadDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM
    # WindTurbineType1or2Dynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM
    # TurbineGovernorDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
