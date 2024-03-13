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
class SynchronousMachineEquivalentCircuit(SynchronousMachineDetailed):
    """
    The electrical equations for all variations of the synchronous models are based on the SynchronousEquivalentCircuit
      diagram for the direct and quadrature axes.    =  +   =  +  *  / ( + )  =  +  * *  / ( *  +  *  +  * )  =  +
      =  +  *  / (+ )  =  +  **  / ( *  +  *  +  * )  = ( + ) / ( * )  = ( *  +  *  +  * ) / ( *  * ( + )  = ( + ) /
      ( * )  = ( *  +  *  +  * )/ ( *  * ( + ) Same equations using CIM attributes from
      SynchronousMachineTimeConstantReactance class on left of = sign and SynchronousMachineEquivalentCircuit class
      on right (except as noted): xDirectSync = xad + RotatingMachineDynamics.statorLeakageReactance xDirectTrans =
      RotatingMachineDynamics.statorLeakageReactance + xad * xfd / (xad + xfd) xDirectSubtrans =
      RotatingMachineDynamics.statorLeakageReactance + xad * xfd * x1d / (xad * xfd + xad * x1d + xfd * x1d)
      xQuadSync = xaq + RotatingMachineDynamics.statorLeakageReactance xQuadTrans =
      RotatingMachineDynamics.statorLeakageReactance + xaq * x1q / (xaq+ x1q) xQuadSubtrans =
      RotatingMachineDynamics.statorLeakageReactance + xaq * x1q* x2q / (xaq * x1q + xaq * x2q + x1q * x2q)  tpdo =
      (xad + xfd) / (2*pi*nominal frequency * rfd) tppdo = (xad * xfd + xad * x1d + xfd * x1d) / (2*pi*nominal
      frequency * r1d * (xad + xfd) tpqo = (xaq + x1q) / (2*pi*nominal frequency * r1q) tppqo = (xaq * x1q + xaq *
      x2q + x1q * x2q)/ (2*pi*nominal frequency * r2q * (xaq + x1q).  Are only valid for a simplified model where
      "Canay" reactance is zero.

    xad: D-axis mutual reactance.
    rfd: Field winding resistance.
    xfd: Field winding leakage reactance.
    r1d: D-axis damper 1 winding resistance.
    x1d: D-axis damper 1 winding leakage reactance.
    xf1d: Differential mutual (`Canay`) reactance.
    xaq: Q-axis mutual reactance.
    r1q: Q-axis damper 1 winding resistance.
    x1q: Q-axis damper 1 winding leakage reactance.
    r2q: Q-axis damper 2 winding resistance.
    x2q: Q-axis damper 2 winding leakage reactance.
    """

    xad : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rfd : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    xfd : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    r1d : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    x1d : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    xf1d : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    xaq : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    r1q : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    x1q : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    r2q : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    x2q : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
