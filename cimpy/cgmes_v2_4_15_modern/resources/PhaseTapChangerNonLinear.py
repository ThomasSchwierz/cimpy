"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .PhaseTapChanger import PhaseTapChanger

@dataclass
class PhaseTapChangerNonLinear(PhaseTapChanger):
    """
    The non-linear phase tap changer describes the non-linear behavior of a phase tap changer. This is a base class for
      the symmetrical and asymmetrical phase tap changer models. The details of these models can be found in the IEC
      61970-301 document.

    voltageStepIncrement: The voltage step increment on the out of phase winding specified in percent of nominal voltage
      of the transformer end.
    xMax: The reactance depend on the tap position according to a `u` shaped curve. The maximum reactance (xMax) appear
      at the low and high tap positions.
    xMin: The reactance depend on the tap position according to a `u` shaped curve. The minimum reactance (xMin) appear
      at the mid tap position.
    """

    voltageStepIncrement : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    xMax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    xMin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ, Profile.SSH,  }
