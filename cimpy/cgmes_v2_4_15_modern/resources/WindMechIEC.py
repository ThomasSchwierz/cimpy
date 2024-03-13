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
class WindMechIEC(IdentifiedObject):
    """
    Two mass model.  Reference: IEC Standard 61400-27-1 Section 6.6.2.1.

    WindGenTurbineType3IEC: Wind turbine Type 3 model with which this wind mechanical model is associated.
    cdrt: Drive train damping (. It is type dependent parameter.
    hgen: Inertia constant of generator (). It is type dependent parameter.
    hwtr: Inertia constant of wind turbine rotor (). It is type dependent parameter.
    kdrt: Drive train stiffness (). It is type dependent parameter.
    WindTurbineType4bIEC: Wind turbine type 4B model with which this wind mechanical model is associated.
    WindTurbineType1or2IEC: Wind generator type 1 or 2 model with which this wind mechanical model is associated.
    """

    # *Association not used*
    # Type M:0..1 in CIM
    # WindGenTurbineType3IEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    cdrt : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    hgen : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    hwtr : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kdrt : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    # *Association not used*
    # Type M:0..1 in CIM
    # WindTurbineType4bIEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

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
