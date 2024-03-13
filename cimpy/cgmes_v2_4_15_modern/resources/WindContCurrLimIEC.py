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
class WindContCurrLimIEC(IdentifiedObject):
    """
    Current limitation model.  The current limitation model combines the physical limits.  Reference: IEC Standard
      61400-27-1 Section 6.6.5.7.

    imax: Maximum continuous current at the wind turbine terminals (). It is type dependent parameter.
    imaxdip: Maximum current during voltage dip at the wind turbine terminals (). It is project dependent parameter.
    mdfslim: Limitation of type 3 stator current  ():  - false=0: total current limitation,  - true=1: stator current
      limitation).  It is type dependent parameter.
    mqpri: Prioritisation of q control during LVRT (): - true = 1: reactive power priority, - false = 0: active power
      priority.  It is project dependent parameter.
    tufilt: Voltage measurement filter time constant (). It is type dependent parameter.
    WindTurbineType3or4IEC: Wind turbine type 3 or 4 model with which this wind control current limitation model is
      associated.
    WindDynamicsLookupTable: The current control limitation model with which this wind dynamics lookup table is
      associated.
    """

    imax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    imaxdip : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    mdfslim : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    mqpri : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tufilt : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    # *Association not used*
    # Type M:1 in CIM
    # WindTurbineType3or4IEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    # *Association not used*
    # Type M:1..n in CIM
    # WindDynamicsLookupTable : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
