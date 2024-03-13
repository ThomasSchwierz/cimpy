"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .WindTurbineType3or4Dynamics import WindTurbineType3or4Dynamics

@dataclass
class WindTurbineType3or4IEC(WindTurbineType3or4Dynamics):
    """
    Parent class supporting relationships to IEC wind turbines Type 3 and 4 and wind plant including their control
      models.

    WindContCurrLimIEC: Wind control current limitation model associated with this wind turbine type 3 or 4 model.
    WIndContQIEC: Wind control Q model associated with this wind turbine type 3 or 4 model.
    WindProtectionIEC: Wind turbune protection model associated with this wind generator type 3 or 4 model.
    """

    WindContCurrLimIEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    WIndContQIEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    WindProtectionIEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
