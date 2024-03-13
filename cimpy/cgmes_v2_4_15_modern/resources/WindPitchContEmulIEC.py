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
class WindPitchContEmulIEC(IdentifiedObject):
    """
    Pitch control emulator model.  Reference: IEC Standard 61400-27-1 Section 6.6.5.1.

    WindGenTurbineType2IEC: Wind turbine type 2 model with which this Pitch control emulator model is associated.
    kdroop: Power error gain (). It is case dependent parameter.
    kipce: Pitch control emulator integral constant (). It is type dependent parameter.
    komegaaero: Aerodynamic power change vs. omegachange (). It is case dependent parameter.
    kppce: Pitch control emulator proportional constant (). It is type dependent parameter.
    omegaref: Rotor speed in initial steady state (omega). It is case dependent parameter.
    pimax: Maximum steady state power (). It is case dependent parameter.
    pimin: Minimum steady state power (). It is case dependent parameter.
    t1: First time constant in pitch control lag (). It is type dependent parameter.
    t2: Second time constant in pitch control lag (). It is type dependent parameter.
    tpe: Time constant in generator air gap power lag (). It is type dependent parameter.
    """

    # *Association not used*
    # Type M:1 in CIM
    # WindGenTurbineType2IEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    kdroop : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kipce : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    komegaaero : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kppce : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    omegaref : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pimax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    pimin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    t2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tpe : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
