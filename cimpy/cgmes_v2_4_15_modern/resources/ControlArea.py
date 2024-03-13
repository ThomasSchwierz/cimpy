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
class ControlArea(PowerSystemResource):
    """
    A control areais a grouping of generating units and/or loads and a cutset of tie lines (as terminals) which may be
      used for a variety of purposes including automatic generation control, powerflow solution area interchange
      control specification, and input to load forecasting.   Note that any number of overlapping control area
      specifications can be superimposed on the physical model.

    EnergyArea: The energy area that is forecast from this control area specification.
    type: The primary type of control area definition used to determine if this is used for automatic generation
      control, for planning interchange control, or other purposes.   A control area specified with primary
      type of automatic generation control could still be forecast and used as an interchange area in power
      flow analysis.
    TieFlow: The tie flows associated with the control area.
    ControlAreaGeneratingUnit: The generating unit specificaitons for the control area.
    netInterchange: The specified positive net interchange into the control area, i.e. positive sign means flow in to
      the area.
    pTolerance: Active power net interchange tolerance
    """

    EnergyArea : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    type : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    # *Association not used*
    # Type M:0..n in CIM
    # TieFlow : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..n in CIM
    # ControlAreaGeneratingUnit : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    netInterchange : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    pTolerance : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ, Profile.SSH,  }
