"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .PFVArControllerType2Dynamics import PFVArControllerType2Dynamics

@dataclass
class PFVArType2IEEEPFController(PFVArControllerType2Dynamics):
    """
    The class represents IEEE PF Controller Type 2 which is a summing point type controller and makes up the outside
      loop of a two-loop system. This controller is implemented as a slow PI type controller. The voltage regulator
      forms the inner loop and is implemented as a fast controller.  Reference: IEEE Standard 421.5-2005 Section
      11.4.

    pfref: Power factor reference ().
    vref: Voltage regulator reference ().
    vclmt: Maximum output of the pf controller ().  Typical Value = 0.1.
    kp: Proportional gain of the pf controller ().  Typical Value = 1.
    ki: Integral gain of the pf controller ().  Typical Value = 1.
    vs: Generator sensing voltage ().
    exlon: Overexcitation or under excitation flag () true = 1 (not in the overexcitation or underexcitation state,
      integral action is active) false = 0 (in the overexcitation or underexcitation state, so integral
      action is disabled to allow the limiter to play its role).
    """

    pfref : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vref : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vclmt : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kp : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ki : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vs : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    exlon : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
