"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcIEEEAC5A(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type AC5A model. The model represents a simplified model for brushless
      excitation systems. The regulator is supplied from a source, such as a permanent magnet generator, which is
      not affected by system disturbances.  Unlike other ac models, this model uses loaded rather than open circuit
      exciter saturation data in the same way as it is used for the dc models.  Because the model has been widely
      implemented by the industry, it is sometimes used to represent other types of systems when either detailed
      data for them are not available or simplified models are required.   Reference: IEEE Standard 421.5-2005
      Section 6.5.

    ka: Voltage regulator gain (K).  Typical Value = 400.
    ta: Voltage regulator time constant (T).  Typical Value = 0.02.
    vrmax: Maximum voltage regulator output (V).  Typical Value = 7.3.
    vrmin: Minimum voltage regulator output (V).  Typical Value = -7.3.
    ke: Exciter constant related to self-excited field (K).  Typical Value = 1.
    te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 0.8.
    kf: Excitation control system stabilizer gains (K).  Typical Value = 0.03.
    tf1: Excitation control system stabilizer time constant (T).  Typical Value = 1.
    tf2: Excitation control system stabilizer time constant (T).  Typical Value = 1.
    tf3: Excitation control system stabilizer time constant (T).  Typical Value = 1.
    efd1: Exciter voltage at which exciter saturation is defined (E).  Typical Value = 5.6.
    seefd1: Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.86.
    efd2: Exciter voltage at which exciter saturation is defined (E).  Typical Value = 4.2.
    seefd2: Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.5.
    """

    ka : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ke : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    te : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kf : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tf1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tf2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tf3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efd1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    seefd1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efd2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    seefd2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
