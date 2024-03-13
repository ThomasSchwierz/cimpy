"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .PowerSystemResource import PowerSystemResource

@dataclass
class RegulatingControl(PowerSystemResource):
    """
    Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.  Remote
      bus voltage control is possible by specifying the controlled terminal located at some place remote from the
      controlling equipment. In case multiple equipment, possibly of different types, control same terminal there
      must be only one RegulatingControl at that terminal. The most specific subtype of RegulatingControl shall be
      used in case such equipment participate in the control, e.g. TapChangerControl for tap changers. For flow
      control  load sign convention is used, i.e. positive sign means flow out from a TopologicalNode (bus) into the
      conducting equipment.

    Terminal: The controls regulating this terminal.
    RegulatingCondEq: The equipment that participates in this regulating control scheme.
    mode: The regulating control mode presently available.  This specification allows for determining the kind of
      regulation without need for obtaining the units from a schedule.
    RegulationSchedule: Schedule for this Regulating regulating control.
    discrete: The regulation is performed in a discrete mode. This applies to equipment with discrete controls, e.g. tap
      changers and shunt compensators.
    enabled: The flag tells if regulation is enabled.
    targetDeadband: This is a deadband used with discrete control to avoid excessive update of controls like tap
      changers and shunt compensator banks while regulating. The units of those appropriate for the
      mode.
    targetValue: The target value specified for case input.   This value can be used for the target value without the
      use of schedules. The value has the units appropriate to the mode attribute.
    targetValueUnitMultiplier: Specify the multiplier for used for the targetValue.
    """

    Terminal : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    # *Association not used*
    # Type M:0..n in CIM
    # RegulatingCondEq : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    mode : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    # *Association not used*
    # Type M:0..n in CIM
    # RegulationSchedule : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    discrete : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    enabled : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    targetDeadband : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    targetValue : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    targetValueUnitMultiplier : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ, Profile.SSH,  }
