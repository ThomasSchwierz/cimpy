"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .ACDCConverter import ACDCConverter

@dataclass
class CsConverter(ACDCConverter):
    """
    DC side of the current source converter (CSC).

    maxAlpha: Maximum firing angle. CSC configuration data used in power flow.
    maxGamma: Maximum extinction angle. CSC configuration data used in power flow.
    maxIdc: The maximum direct current (Id) on the DC side at which the converter should operate. Converter
      configuration data use in power flow.
    minAlpha: Minimum firing angle. CSC configuration data used in power flow.
    minGamma: Minimum extinction angle. CSC configuration data used in power flow.
    minIdc: The minimum direct current (Id) on the DC side at which the converter should operate. CSC configuration data
      used in power flow.
    ratedIdc: Rated converter DC current, also called IdN. Converter configuration data used in power flow.
    alpha: Firing angle, typical value between 10 and 18 degrees for a rectifier. CSC state variable, result from power
      flow.
    gamma: Extinction angle. CSC state variable, result from power flow.
    operatingMode: Indicates whether the DC pole is operating as an inverter or as a rectifier. CSC control variable
      used in power flow.
    pPccControl: 
    targetAlpha: Target firing angle. CSC control variable used in power flow.
    targetGamma: Target extinction angle. CSC  control variable used in power flow.
    targetIdc: DC current target value. CSC control variable used in power flow.
    """

    maxAlpha : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    maxGamma : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    maxIdc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    minAlpha : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    minGamma : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    minIdc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    ratedIdc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    alpha : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SV, ]}) 

    gamma : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SV, ]}) 

    operatingMode : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    pPccControl : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    targetAlpha : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    targetGamma : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    targetIdc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ, Profile.SV, Profile.SSH,  }
