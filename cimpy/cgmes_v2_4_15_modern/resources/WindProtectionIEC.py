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
class WindProtectionIEC(IdentifiedObject):
    """
    The grid protection model includes protection against over and under voltage, and against over and under frequency.
      Reference: IEC Standard 614000-27-1 Section 6.6.6.

    fover: Set of wind turbine over frequency protection levels (). It is project dependent parameter.
    funder: Set of wind turbine under frequency protection levels (). It is project dependent parameter.
    tfover: Set of corresponding wind turbine over frequency protection disconnection times (). It is project dependent
      parameter.
    tfunder: Set of corresponding wind turbine under frequency protection disconnection times (). It is project
      dependent parameter.
    tuover: Set of corresponding wind turbine over voltage protection disconnection times (). It is project dependent
      parameter.
    tuunder: Set of corresponding wind turbine under voltage protection disconnection times (). It is project dependent
      parameter.
    uover: Set of wind turbine over voltage protection levels (). It is project dependent parameter.
    uunder: Set of wind turbine under voltage protection levels (). It is project dependent parameter.
    WindTurbineType3or4IEC: Wind generator type 3 or 4 model with which this wind turbine protection model is
      associated.
    WindTurbineType1or2IEC: Wind generator type 1 or 2 model with which this wind turbine protection model is
      associated.
    """

    fover : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    funder : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tfover : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tfunder : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tuover : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tuunder : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    uover : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    uunder : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    # *Association not used*
    # Type M:0..1 in CIM
    # WindTurbineType3or4IEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM
    # WindTurbineType1or2IEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
