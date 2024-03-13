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
class WindPlantReactiveControlIEC(IdentifiedObject):
    """
    Simplified plant voltage and reactive power control model for use with type 3 and type 4 wind turbine models.
      Reference: IEC Standard 61400-27-1 Annex E.

    WindPlantIEC: Wind plant model with which this wind reactive control is associated.
    kiwpx: Plant Q controller integral gain (). It is type dependent parameter.
    kpwpx: Plant Q controller proportional gain (). It is type dependent parameter.
    kwpqu: Plant voltage control droop (). It is project dependent parameter.
    mwppf: Power factor control modes selector (). Used only if mwpu is set to false. true = 1: power factor control
      false = 0: reactive power control. It is project dependent parameter.
    mwpu: Reactive power control modes selector (). true = 1: voltage control false = 0: reactive power control. It is
      project dependent parameter.
    twppfilt: Filter time constant for active power measurement (). It is type dependent parameter.
    twpqfilt: Filter time constant for reactive power measurement (). It is type dependent parameter.
    twpufilt: Filter time constant for voltage measurement (). It is type dependent parameter.
    txft: Lead time constant in reference value transfer function (). It is type dependent parameter.
    txfv: Lag time constant in reference value transfer function (). It is type dependent parameter.
    uwpqdip: Voltage threshold for LVRT detection in q control (). It is type dependent parameter.
    xrefmax: Maximum  ( or delta ) request from the plant controller (). It is project dependent parameter.
    xrefmin: Minimum  ( or delta) request from the plant controller (). It is project dependent parameter.
    """

    # *Association not used*
    # Type M:1 in CIM
    # WindPlantIEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    kiwpx : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kpwpx : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kwpqu : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    mwppf : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    mwpu : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    twppfilt : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    twpqfilt : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    twpufilt : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    txft : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    txfv : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    uwpqdip : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    xrefmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    xrefmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
