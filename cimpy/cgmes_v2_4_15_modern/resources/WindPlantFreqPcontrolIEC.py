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
class WindPlantFreqPcontrolIEC(IdentifiedObject):
    """
    Frequency and active power controller model.  Reference: IEC Standard 61400-27-1 Annex E.

    WindDynamicsLookupTable: The frequency and active power wind plant control model with which this wind dynamics
      lookup table is associated.
    dprefmax: Maximum ramp rate of  request from the plant controller to the wind turbines (). It is project dependent
      parameter.
    dprefmin: Minimum (negative) ramp rate of  request from the plant controller to the wind turbines (). It is project
      dependent parameter.
    kiwpp: Plant P controller integral gain (). It is type dependent parameter.
    kpwpp: Plant P controller proportional gain (). It is type dependent parameter.
    prefmax: Maximum  request from the plant controller to the wind turbines (). It is type dependent parameter.
    prefmin: Minimum  request from the plant controller to the wind turbines (). It is type dependent parameter.
    tpft: Lead time constant in reference value transfer function (). It is type dependent parameter.
    tpfv: Lag time constant in reference value transfer function (). It is type dependent parameter.
    twpffilt: Filter time constant for frequency measurement (). It is type dependent parameter.
    twppfilt: Filter time constant for active power measurement (). It is type dependent parameter.
    WindPlantIEC: Wind plant model with which this wind plant frequency and active power control is associated.
    """

    # *Association not used*
    # Type M:1..n in CIM
    # WindDynamicsLookupTable : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    dprefmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    dprefmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kiwpp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kpwpp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    prefmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    prefmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tpft : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tpfv : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    twpffilt : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    twppfilt : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    # *Association not used*
    # Type M:1 in CIM
    # WindPlantIEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
