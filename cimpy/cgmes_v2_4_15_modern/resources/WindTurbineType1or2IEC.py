"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .WindTurbineType1or2Dynamics import WindTurbineType1or2Dynamics

@dataclass
class WindTurbineType1or2IEC(WindTurbineType1or2Dynamics):
    """
    Generator model for wind turbine of IEC Type 1 or Type 2 is a standard asynchronous generator model.  Reference: IEC
      Standard 614000-27-1 Section 6.6.3.1.

    WindMechIEC: Wind mechanical model associated with this wind generator type 1 or 2 model.
    WindProtectionIEC: Wind turbune protection model associated with this wind generator type 1 or 2 model.
    """

    WindMechIEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    WindProtectionIEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
