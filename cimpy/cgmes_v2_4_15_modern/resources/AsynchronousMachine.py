"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .RotatingMachine import RotatingMachine

@dataclass
class AsynchronousMachine(RotatingMachine):
    """
    A rotating machine whose shaft rotates asynchronously with the electrical field.  Also known as an induction machine
      with no external connection to the rotor windings, e.g squirrel-cage induction machine.

    AsynchronousMachineDynamics: Asynchronous machine dynamics model used to describe dynamic behavior of this
      asynchronous machine.
    converterFedDrive: Indicates whether the machine is a converter fed drive. Used for short circuit data exchange
      according to IEC 60909
    efficiency: Efficiency of the asynchronous machine at nominal operation in percent. Indicator for converter drive
      motors. Used for short circuit data exchange according to IEC 60909
    iaIrRatio: Ratio of locked-rotor current to the rated current of the motor (Ia/Ir). Used for short circuit data
      exchange according to IEC 60909
    nominalFrequency: Nameplate data indicates if the machine is 50 or 60 Hz.
    nominalSpeed: Nameplate data.  Depends on the slip and number of pole pairs.
    polePairNumber: Number of pole pairs of stator. Used for short circuit data exchange according to IEC 60909
    ratedMechanicalPower: Rated mechanical power (Pr in the IEC 60909-0). Used for short circuit data exchange according
      to IEC 60909.
    reversible: Indicates for converter drive motors if the power can be reversible. Used for short circuit data
      exchange according to IEC 60909
    rxLockedRotorRatio: Locked rotor ratio (R/X). Used for short circuit data exchange according to IEC 60909
    asynchronousMachineType: Indicates the type of Asynchronous Machine (motor or generator).
    """

    # *Association not used*
    # Type M:0..1 in CIM
    # AsynchronousMachineDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    converterFedDrive : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    efficiency : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    iaIrRatio : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    nominalFrequency : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    nominalSpeed : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    polePairNumber : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    ratedMechanicalPower : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    reversible : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    rxLockedRotorRatio : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    asynchronousMachineType : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY, Profile.EQ, Profile.SSH,  }
