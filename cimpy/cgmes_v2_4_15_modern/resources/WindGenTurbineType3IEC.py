"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .WindTurbineType3or4IEC import WindTurbineType3or4IEC

@dataclass
class WindGenTurbineType3IEC(WindTurbineType3or4IEC):
    """
    Generator model for wind turbines of IEC type 3A and 3B.

    WindAeroLinearIEC: Wind aerodynamic model associated with this wind generator type 3 model.
    WindContPitchAngleIEC: Wind control pitch angle model associated with this wind turbine type 3.
    WindContPType3IEC: Wind control P type 3 model associated with this wind turbine type 3 model.
    dipmax: Maximum active current ramp rate (di). It is project dependent parameter.
    diqmax: Maximum reactive current ramp rate (di). It is project dependent parameter.
    WindMechIEC: Wind mechanical model associated with this wind turbine Type 3 model.
    """

    WindAeroLinearIEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    WindContPitchAngleIEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    WindContPType3IEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    dipmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    diqmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    WindMechIEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
