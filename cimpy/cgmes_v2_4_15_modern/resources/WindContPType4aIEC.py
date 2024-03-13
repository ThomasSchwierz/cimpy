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
class WindContPType4aIEC(IdentifiedObject):
    """
    P control model Type 4A.  Reference: IEC Standard 61400-27-1 Section 6.6.5.4.

    dpmax: Maximum wind turbine power ramp rate (). It is project dependent parameter.
    tpord: Time constant in power order lag (). It is type dependent parameter.
    tufilt: Voltage measurement filter time constant (). It is type dependent parameter.
    WindTurbineType4aIEC: Wind turbine type 4A model with which this wind control P type 4A model is associated.
    """

    dpmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tpord : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tufilt : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    # *Association not used*
    # Type M:1 in CIM
    # WindTurbineType4aIEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
