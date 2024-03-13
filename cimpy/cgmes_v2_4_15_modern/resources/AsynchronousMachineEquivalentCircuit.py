"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .AsynchronousMachineDynamics import AsynchronousMachineDynamics

@dataclass
class AsynchronousMachineEquivalentCircuit(AsynchronousMachineDynamics):
    """
    The electrical equations of all variations of the asynchronous model are based on the AsynchronousEquivalentCircuit
      diagram for the direct and quadrature axes, with two equivalent rotor windings in each axis.      =  +   =  +
      *  / ( + )  =  +  * *  / ( *  +  *  +  * )  = ( + ) / ( * )  = ( *  +  *  +  * ) / ( *  * (+ ) Same equations
      using CIM attributes from AsynchronousMachineTimeConstantReactance class on left of = sign and
      AsynchronousMachineEquivalentCircuit class on right (except as noted): xs = xm +
      RotatingMachineDynamics.statorLeakageReactance xp = RotatingMachineDynamics.statorLeakageReactance + xm * xlr1
      / (xm + xlr1) xpp = RotatingMachineDynamics.statorLeakageReactance + xm * xlr1* xlr2 / (xm * xlr1 + xm * xlr2
      + xlr1 * xlr2) tpo = (xm + xlr1) / (2*pi*nominal frequency * rr1) tppo = (xm * xlr1 + xm * xlr2 + xlr1 * xlr2)
      / (2*pi*nominal frequency * rr2 * (xm + xlr1).

    xm: Magnetizing reactance.
    rr1: Damper 1 winding resistance.
    xlr1: Damper 1 winding leakage reactance.
    rr2: Damper 2 winding resistance.
    xlr2: Damper 2 winding leakage reactance.
    """

    xm : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rr1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    xlr1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    rr2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    xlr2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
