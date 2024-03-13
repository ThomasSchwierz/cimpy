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
class WindAeroConstIEC(IdentifiedObject):
    """
    The constant aerodynamic torque model assumes that the aerodynamic torque is constant.  Reference: IEC Standard
      61400-27-1 Section 6.6.1.1.

    WindGenTurbineType1IEC: Wind turbine type 1 model with which this wind aerodynamic model is associated.
    """

    # *Association not used*
    # Type M:1 in CIM
    # WindGenTurbineType1IEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
