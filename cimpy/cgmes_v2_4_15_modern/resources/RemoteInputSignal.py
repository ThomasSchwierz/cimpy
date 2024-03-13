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
class RemoteInputSignal(IdentifiedObject):
    """
    Supports connection to a terminal associated with a remote bus from which an input signal of a specific type is
      coming.

    Terminal: Remote terminal with which this input signal is associated.
    remoteSignalType: Type of input signal.
    PFVArControllerType1Dynamics: Power Factor or VAr controller Type I model using this remote input signal.
    UnderexcitationLimiterDynamics: Underexcitation limiter model using this remote input signal.
    WindTurbineType1or2Dynamics: Wind generator Type 1 or Type 2 model using this remote input signal.
    VoltageCompensatorDynamics: Voltage compensator model using this remote input signal.
    PowerSystemStabilizerDynamics: Power system stabilizer model using this remote input signal.
    DiscontinuousExcitationControlDynamics: Discontinuous excitation control model using this remote input signal.
    WindTurbineType3or4Dynamics: Remote input signal used by these wind turbine Type 3 or 4 models.
    WindPlantDynamics: The remote signal with which this power plant is associated.
    """

    Terminal : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    remoteSignalType : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    PFVArControllerType1Dynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    UnderexcitationLimiterDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    # *Association not used*
    # Type M:0..1 in CIM
    # WindTurbineType1or2Dynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    VoltageCompensatorDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    PowerSystemStabilizerDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    DiscontinuousExcitationControlDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    # *Association not used*
    # Type M:0..1 in CIM
    # WindTurbineType3or4Dynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM
    # WindPlantDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
