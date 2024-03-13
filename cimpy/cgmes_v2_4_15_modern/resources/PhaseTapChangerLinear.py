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
class PhaseTapChangerLinear(PhaseTapChanger):
    """
    Describes a tap changer with a linear relation between the tap step and the phase angle difference across the
      transformer. This is a mathematical model that is an approximation of a real phase tap changer. The phase
      angle is computed as stepPhaseShitfIncrement times the tap position. The secondary side voltage magnitude is
      the same as at the primary side.

    stepPhaseShiftIncrement: Phase shift per step position. A positive value indicates a positive phase shift from the
      winding where the tap is located to the other winding (for a two-winding
      transformer). The actual phase shift increment might be more accurately computed from
      the symmetrical or asymmetrical models or a tap step table lookup if those are
      available.
    xMax: The reactance depend on the tap position according to a `u` shaped curve. The maximum reactance (xMax) appear
      at the low and high tap positions.
    xMin: The reactance depend on the tap position according to a `u` shaped curve. The minimum reactance (xMin) appear
      at the mid tap position.
    """

    stepPhaseShiftIncrement : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    xMax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    xMin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ, Profile.SSH,  }
