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
class WindContRotorRIEC(IdentifiedObject):
    """
    Rotor resistance control model.  Reference: IEC Standard 61400-27-1 Section 6.6.5.2.

    kirr: Integral gain in rotor resistance PI controller (). It is type dependent parameter.
    komegafilt: Filter gain for generator speed measurement (K). It is type dependent parameter.
    kpfilt: Filter gain for power measurement (). It is type dependent parameter.
    kprr: Proportional gain in rotor resistance PI controller (). It is type dependent parameter.
    rmax: Maximum rotor resistance (). It is type dependent parameter.
    rmin: Minimum rotor resistance (). It is type dependent parameter.
    tomegafilt: Filter time constant for generator speed measurement (). It is type dependent parameter.
    tpfilt: Filter time constant for power measurement (). It is type dependent parameter.
    WindDynamicsLookupTable: The wind dynamics lookup table associated with this rotor resistance control model.
    WindGenTurbineType2IEC: Wind turbine type 2 model with whitch this wind control rotor resistance model is
      associated.
    """

    kirr : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    komegafilt : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kpfilt : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kprr : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tomegafilt : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tpfilt : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    # *Association not used*
    # Type M:1..n in CIM
    # WindDynamicsLookupTable : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    # *Association not used*
    # Type M:1 in CIM
    # WindGenTurbineType2IEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
