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
class WindAeroLinearIEC(IdentifiedObject):
    """
    The linearised aerodynamic model.    Reference: IEC Standard 614000-27-1 Section 6.6.1.2.

    dpomega: Partial derivative of aerodynamic power with respect to changes in WTR speed (). It is case dependent
      parameter.
    dptheta: Partial derivative of aerodynamic power with respect to changes in pitch angle (). It is case dependent
      parameter.
    omegazero: Rotor speed if the wind turbine is not derated (). It is case dependent parameter.
    pavail: Available aerodynamic power (). It is case dependent parameter.
    thetazero: Pitch angle if the wind turbine is not derated (). It is case dependent parameter.
    WindGenTurbineType3IEC: Wind generator type 3 model with which this wind aerodynamic model is associated.
    """

    dpomega : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    dptheta : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    omegazero : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pavail : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    thetazero : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    # *Association not used*
    # Type M:1 in CIM
    # WindGenTurbineType3IEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
