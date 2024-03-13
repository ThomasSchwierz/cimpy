"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .WindTurbineType1or2IEC import WindTurbineType1or2IEC

@dataclass
class WindGenTurbineType2IEC(WindTurbineType1or2IEC):
    """
    Wind turbine IEC Type 2.  Reference: IEC Standard 61400-27-1, section 6.5.3.

    WindContRotorRIEC: Wind control rotor resistance model associated with wind turbine type 2 model.
    WindPitchContEmulIEC: Pitch control emulator model associated with this wind turbine type 2 model.
    """

    WindContRotorRIEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    WindPitchContEmulIEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
