"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from ..utils.base import Base

@dataclass
class TieFlow(Base):
    """
    A flow specification in terms of location and direction for a control area.

    Terminal: The terminal to which this tie flow belongs.
    ControlArea: The control area of the tie flows.
    positiveFlowIn: True if the flow into the terminal (load convention) is also flow into the control area.  For
      example, this attribute should be true if using the tie line terminal further away from the
      control area. For example to represent a tie to a shunt component (like a load or generator)
      in another area, this is the near end of a branch and this attribute would be specified as
      false.
    """

    Terminal : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    ControlArea : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    positiveFlowIn : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
