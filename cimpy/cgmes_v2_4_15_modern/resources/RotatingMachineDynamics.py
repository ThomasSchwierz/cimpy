"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .DynamicsFunctionBlock import DynamicsFunctionBlock

@dataclass
class RotatingMachineDynamics(DynamicsFunctionBlock):
    """
    Abstract parent class for all synchronous and asynchronous machine standard models.

    damping: Damping torque coefficient (D).  A proportionality constant that, when multiplied by the angular velocity
      of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.
      This value is often zero when the sources of damping torques (generator damper windings, load damping
      effects, etc.) are modelled in detail.  Typical Value = 0.
    inertia: Inertia constant of generator or motor and mechanical load (H) (>0).  This is the specification for the
      stored energy in the rotating mass when operating at rated speed.  For a generator, this includes the
      generator plus all other elements (turbine, exciter) on the same shaft and has units of MW*sec.  For
      a motor, it includes the motor plus its mechanical load. Conventional units are per unit on the
      generator MVA base, usually expressed as MW*second/MVA or just second.   This value is used in the
      accelerating power reference frame for operator training simulator solutions.  Typical Value = 3.
    saturationFactor: Saturation factor at rated terminal voltage (S1) (> or =0).  Not used by simplified model.
      Defined by defined by S(E1) in the SynchronousMachineSaturationParameters diagram.  Typical
      Value = 0.02.
    saturationFactor120: Saturation factor at 120% of rated terminal voltage (S12) (> or =S1). Not used by the
      simplified model, defined by S(E2) in the SynchronousMachineSaturationParameters diagram.
      Typical Value = 0.12.
    statorLeakageReactance: Stator leakage reactance (Xl) (> or =0). Typical Value = 0.15.
    statorResistance: Stator (armature) resistance (Rs) (> or =0). Typical Value = 0.005.
    """

    damping : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    inertia : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    saturationFactor : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    saturationFactor120 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    statorLeakageReactance : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    statorResistance : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
