"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .SynchronousMachineDetailed import SynchronousMachineDetailed

@dataclass
class SynchronousMachineTimeConstantReactance(SynchronousMachineDetailed):
    """
    Synchronous machine detailed modelling types are defined by the combination of the attributes
      SynchronousMachineTimeConstantReactance.modelType and SynchronousMachineTimeConstantReactance.rotorType.
      The parameters used for models expressed in time constant reactance form include:

    rotorType: Type of rotor on physical machine.
    modelType: Type of synchronous machine model used in Dynamic simulation applications.
    ks: Saturation loading correction factor (Ks) (>= 0).  Used only by Type J model.  Typical Value = 0.
    xDirectSync: Direct-axis synchronous reactance (Xd) (>= X`d). The quotient of a sustained value of that AC component
      of armature voltage that is produced by the total direct-axis flux due to direct-axis armature
      current and the value of the AC component of this current, the machine running at rated speed.
      Typical Value = 1.8.
    xDirectTrans: Direct-axis transient reactance (unsaturated) (X`d) (> =X``d).  Typical Value = 0.5.
    xDirectSubtrans: Direct-axis subtransient reactance (unsaturated) (X``d) (> Xl).  Typical Value = 0.2.
    xQuadSync: Quadrature-axis synchronous reactance (Xq) (> =X`q). The ratio of the component of reactive armature
      voltage, due to the quadrature-axis component of armature current, to this component of current,
      under steady state conditions and at rated frequency.  Typical Value = 1.6.
    xQuadTrans: Quadrature-axis transient reactance (X`q) (> =X``q).  Typical Value = 0.3.
    xQuadSubtrans: Quadrature-axis subtransient reactance (X``q) (> Xl).  Typical Value = 0.2.
    tpdo: Direct-axis transient rotor time constant (T`do) (> T``do).  Typical Value = 5.
    tppdo: Direct-axis subtransient rotor time constant (T``do) (> 0).  Typical Value = 0.03.
    tpqo: Quadrature-axis transient rotor time constant (T`qo) (> T``qo). Typical Value = 0.5.
    tppqo: Quadrature-axis subtransient rotor time constant (T``qo) (> 0). Typical Value = 0.03.
    tc: Damping time constant for `Canay` reactance.  Typical Value = 0.
    """

    rotorType : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    modelType : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ks : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    xDirectSync : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    xDirectTrans : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    xDirectSubtrans : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    xQuadSync : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    xQuadTrans : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    xQuadSubtrans : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tpdo : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tppdo : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tpqo : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tppqo : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
