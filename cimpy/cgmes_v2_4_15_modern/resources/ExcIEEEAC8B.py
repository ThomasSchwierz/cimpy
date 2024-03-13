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
class ExcIEEEAC8B(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type AC8B model. This model represents a PID voltage regulator with either
      a brushless exciter or dc exciter. The AVR in this model consists of PID control, with separate constants for
      the proportional (), integral (), and derivative () gains. The representation of the brushless exciter (, , ,
      , ) is similar to the model Type AC2A. The Type AC8B model can be used to represent static voltage regulators
      applied to brushless excitation systems. Digitally based voltage regulators feeding dc rotating main exciters
      can be represented with the AC Type AC8B model with the parameters  and  set to 0.  For thyristor power stages
      fed from the generator terminals, the limits  and  should be a function of terminal voltage:  * and  * .
      Reference: IEEE Standard 421.5-2005 Section 6.8.

    kpr: Voltage regulator proportional gain (K).  Typical Value = 80.
    kir: Voltage regulator integral gain (K).  Typical Value = 5.
    kdr: Voltage regulator derivative gain (K).  Typical Value = 10.
    tdr: Lag time constant (T).  Typical Value = 0.1.
    vrmax: Maximum voltage regulator output (V).  Typical Value = 35.
    vrmin: Minimum voltage regulator output (V).  Typical Value = 0.
    ka: Voltage regulator gain (K).  Typical Value = 1.
    ta: Voltage regulator time constant (T).  Typical Value = 0.
    te: Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 1.2.
    vfemax: Exciter field current limit reference (V).  Typical Value = 6.
    vemin: Minimum exciter voltage output (V).  Typical Value = 0.
    ke: Exciter constant related to self-excited field (K).  Typical Value = 1.
    kc: Rectifier loading factor proportional to commutating reactance (K). Typical Value = 0.55.
    kd: Demagnetizing factor, a function of exciter alternator reactances (K).    Typical Value = 1.1.
    ve1: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V) equals V
      (V).  Typical Value = 6.5.
    seve1: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance
      (S[V]).  Typical Value = 0.3.
    ve2: Exciter alternator output voltages back of commutating reactance at which saturation is defined (V).  Typical
      Value = 9.
    seve2: Exciter saturation function value at the corresponding exciter voltage, V, back of commutating reactance
      (S[V]).  Typical Value = 3.
    """

    kpr : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kir : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kdr : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tdr : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ka : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ta : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    te : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vfemax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vemin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ke : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kc : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kd : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ve1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    seve1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ve2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    seve2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
