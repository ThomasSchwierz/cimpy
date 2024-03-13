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
class SynchronousMachine(RotatingMachine):
    """
    An electromechanical device that operates with shaft rotating synchronously with the network. It is a single machine
      operating either as a generator or synchronous condenser or pump.

    SynchronousMachineDynamics: Synchronous machine dynamics model used to describe dynamic behavior of this synchronous
      machine.
    InitialReactiveCapabilityCurve: Synchronous machines using this curve as default.
    earthing: Indicates whether or not the generator is earthed. Used for short circuit data exchange according to IEC
      60909
    earthingStarPointR: Generator star point earthing resistance (Re). Used for short circuit data exchange according to
      IEC 60909
    earthingStarPointX: Generator star point earthing reactance (Xe). Used for short circuit data exchange according to
      IEC 60909
    ikk: Steady-state short-circuit current (in A for the profile) of generator with compound excitation during 3-phase
      short circuit. - Ikk=0: Generator with no compound excitation. - Ikk?0: Generator with compound
      excitation. Ikk is used to calculate the minimum steady-state short-circuit current for generators with
      compound excitation (Section 4.6.1.2 in the IEC 60909-0) Used only for single fed short circuit on a
      generator. (Section 4.3.4.2. in the IEC 60909-0)
    maxQ: Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.
    minQ: Minimum reactive power limit for the unit.
    mu: Factor to calculate the breaking current (Section 4.5.2.1 in the IEC 60909-0). Used only for single fed short
      circuit on a generator (Section 4.3.4.2. in the IEC 60909-0).
    qPercent: Percent of the coordinated reactive control that comes from this machine.
    r0: Zero sequence resistance of the synchronous machine.
    r2: Negative sequence resistance.
    satDirectSubtransX: Direct-axis subtransient reactance saturated, also known as Xd`sat.
    satDirectSyncX: Direct-axes saturated synchronous reactance (xdsat); reciprocal of short-circuit ration. Used for
      short circuit data exchange, only for single fed short circuit on a generator. (Section
      4.3.4.2. in the IEC 60909-0).
    satDirectTransX: Saturated Direct-axis transient reactance. The attribute is primarily used for short circuit
      calculations according to ANSI.
    shortCircuitRotorType: Type of rotor, used by short circuit applications, only for single fed short circuit
      according to IEC 60909.
    type: Modes that this synchronous machine can operate in.
    voltageRegulationRange: Range of generator voltage regulation (PG in the IEC 60909-0) used for calculation of the
      impedance correction factor KG defined in IEC 60909-0 This attribute is used to
      describe the operating voltage of the generating unit.
    r: Equivalent resistance (RG) of generator. RG is considered for the calculation of all currents, except for the
      calculation of the peak current ip. Used for short circuit data exchange according to IEC 60909
    x0: Zero sequence reactance of the synchronous machine.
    x2: Negative sequence reactance.
    operatingMode: Current mode of operation.
    referencePriority: Priority of unit for use as powerflow voltage phase angle reference bus selection. 0 = don t care
      (default) 1 = highest priority. 2 is less than 1 and so on.
    """

    # *Association not used*
    # Type M:0..1 in CIM
    # SynchronousMachineDynamics : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    InitialReactiveCapabilityCurve : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    earthing : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    earthingStarPointR : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    earthingStarPointX : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    ikk : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    maxQ : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    minQ : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    mu : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    qPercent : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    r0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    r2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    satDirectSubtransX : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    satDirectSyncX : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    satDirectTransX : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    shortCircuitRotorType : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    type : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    voltageRegulationRange : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    r : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    x0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    x2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    operatingMode : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    referencePriority : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY, Profile.EQ, Profile.SSH,  }
