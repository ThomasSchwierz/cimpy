"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from ..utils.base import Base

@dataclass
class ProprietaryParameterDynamics(Base):
    """
    Supports definition of one or more parameters of several different datatypes for use by proprietary user-defined
      models.  NOTE: This class does not inherit from IdentifiedObject since it is not intended that a single
      instance of it be referenced by more than one proprietary user-defined model instance.

    WindPlantUserDefined: Proprietary user-defined model with which this parameter is associated.
    WindType1or2UserDefined: Proprietary user-defined model with which this parameter is associated.
    WindType3or4UserDefined: Proprietary user-defined model with which this parameter is associated.
    SynchronousMachineUserDefined: Proprietary user-defined model with which this parameter is associated.
    AsynchronousMachineUserDefined: Proprietary user-defined model with which this parameter is associated.
    TurbineGovernorUserDefined: Proprietary user-defined model with which this parameter is associated.
    TurbineLoadControllerUserDefined: Proprietary user-defined model with which this parameter is associated.
    MechanicalLoadUserDefined: Proprietary user-defined model with which this parameter is associated.
    ExcitationSystemUserDefined: Proprietary user-defined model with which this parameter is associated.
    OverexcitationLimiterUserDefined: Proprietary user-defined model with which this parameter is associated.
    UnderexcitationLimiterUserDefined: Proprietary user-defined model with which this parameter is associated.
    PowerSystemStabilizerUserDefined: Proprietary user-defined model with which this parameter is associated.
    DiscontinuousExcitationControlUserDefined: Proprietary user-defined model with which this parameter is associated.
    PFVArControllerType1UserDefined: Proprietary user-defined model with which this parameter is associated.
    VoltageAdjusterUserDefined: Proprietary user-defined model with which this parameter is associated.
    PFVArControllerType2UserDefined: Proprietary user-defined model with which this parameter is associated.
    VoltageCompensatorUserDefined: Proprietary user-defined model with which this parameter is associated.
    LoadUserDefined: Proprietary user-defined model with which this parameter is associated.
    parameterNumber: Sequence number of the parameter among the set of parameters associated with the related
      proprietary user-defined model.
    booleanParameterValue: Used for boolean parameter value. If this attribute is populated, integerParameterValue and
      floatParameterValue will not be.
    integerParameterValue: Used for integer parameter value.  If this attribute is populated, booleanParameterValue and
      floatParameterValue will not be.
    floatParameterValue: Used for floating point parameter value.  If this attribute is populated, booleanParameterValue
      and integerParameterValue will not be.
    """

    WindPlantUserDefined : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    WindType1or2UserDefined : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    WindType3or4UserDefined : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    SynchronousMachineUserDefined : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    AsynchronousMachineUserDefined : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    TurbineGovernorUserDefined : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    TurbineLoadControllerUserDefined : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    MechanicalLoadUserDefined : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ExcitationSystemUserDefined : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    OverexcitationLimiterUserDefined : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    UnderexcitationLimiterUserDefined : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    PowerSystemStabilizerUserDefined : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    DiscontinuousExcitationControlUserDefined : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    PFVArControllerType1UserDefined : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    VoltageAdjusterUserDefined : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    PFVArControllerType2UserDefined : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    VoltageCompensatorUserDefined : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    LoadUserDefined : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    parameterNumber : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    booleanParameterValue : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    integerParameterValue : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    floatParameterValue : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
