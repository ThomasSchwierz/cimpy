"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .PFVArControllerType1Dynamics import PFVArControllerType1Dynamics

@dataclass
class PFVArType1IEEEPFController(PFVArControllerType1Dynamics):
    """
    The class represents IEEE PF Controller Type 1 which operates by moving the voltage reference directly.  Reference:
      IEEE Standard 421.5-2005 Section 11.2.

    ovex: Overexcitation Flag () true = overexcited false = underexcited.
    tpfc: PF controller time delay ().  Typical Value = 5.
    vitmin: Minimum machine terminal current needed to enable pf/var controller ().
    vpf: Synchronous machine power factor ().
    vpfcbw: PF controller dead band ().  Typical Value = 0.05.
    vpfref: PF controller reference ().
    vvtmax: Maximum machine terminal voltage needed for pf/var controller to be enabled ().
    vvtmin: Minimum machine terminal voltage needed to enable pf/var controller ().
    """

    ovex : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tpfc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vitmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vpf : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vpfcbw : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vpfref : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vvtmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vvtmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
