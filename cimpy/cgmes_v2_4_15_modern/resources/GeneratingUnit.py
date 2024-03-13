"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .Equipment import Equipment

@dataclass
class GeneratingUnit(Equipment):
    """
    A single or set of synchronous machines for converting mechanical power into alternating-current power. For example,
      individual machines within a set may be defined for scheduling purposes while a single control signal is
      derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional
      GeneratingUnit corresponding to the set.

    genControlSource: The source of controls for a generating unit.
    governorSCD: Governor Speed Changer Droop.   This is the change in generator power output divided by the change in
      frequency normalized by the nominal power of the generator and the nominal frequency and
      expressed in percent and negated. A positive value of speed change droop provides additional
      generator output upon a drop in frequency.
    initialP: Default initial active power  which is used to store a powerflow result for the initial active power for
      this unit in this network configuration.
    longPF: Generating unit long term economic participation factor.
    maximumAllowableSpinningReserve: Maximum allowable spinning reserve. Spinning reserve will never be considered
      greater than this value regardless of the current operating point.
    maxOperatingP: This is the maximum operating active power limit the dispatcher can enter for this unit.
    minOperatingP: This is the minimum operating active power limit the dispatcher can enter for this unit.
    nominalP: The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes
      such as the governor speed change droop (governorSCD attribute). The attribute shall be a positive
      value equal or less than RotatingMachine.ratedS.
    ratedGrossMaxP: The unit`s gross rated maximum capacity (book value).
    ratedGrossMinP: The gross rated minimum generation level which the unit can safely operate at while delivering power
      to the transmission grid.
    ratedNetMaxP: The net rated maximum capacity determined by subtracting the auxiliary power used to operate the
      internal plant machinery from the rated gross maximum capacity.
    shortPF: Generating unit short term economic participation factor.
    startupCost: The initial startup cost incurred for each start of the GeneratingUnit.
    variableCost: The variable cost component of production per unit of ActivePower.
    totalEfficiency: The efficiency of the unit in converting the fuel into electrical energy.
    ControlAreaGeneratingUnit: ControlArea specifications for this generating unit.
    RotatingMachine: A synchronous machine may operate as a generator and as such becomes a member of a generating unit.
    GrossToNetActivePowerCurves: A generating unit may have a gross active power to net active power curve, describing
      the losses and auxiliary power requirements of the unit.
    normalPF: Generating unit economic participation factor.
    """

    genControlSource : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    governorSCD : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    initialP : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    longPF : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    maximumAllowableSpinningReserve : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    maxOperatingP : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    minOperatingP : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    nominalP : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    ratedGrossMaxP : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    ratedGrossMinP : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    ratedNetMaxP : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    shortPF : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    startupCost : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    variableCost : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    totalEfficiency : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    # *Association not used*
    # Type M:0..n in CIM
    # ControlAreaGeneratingUnit : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    # *Association not used*
    # Type M:1..n in CIM
    # RotatingMachine : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..n in CIM
    # GrossToNetActivePowerCurves : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    normalPF : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ, Profile.SSH,  }
