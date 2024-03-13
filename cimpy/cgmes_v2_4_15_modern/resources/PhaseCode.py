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
class PhaseCode(Base):
    """
    Enumeration of phase identifiers. Allows designation of phases for both transmission and distribution equipment,
      circuits and loads. Residential and small commercial loads are often served from single-phase, or split-phase,
      secondary circuits. For example of s12N, phases 1 and 2 refer to hot wires that are 180 degrees out of phase,
      while N refers to the neutral wire. Through single-phase transformer connections, these secondary circuits may
      be served from one or two of the primary phases A, B, and C. For three-phase loads, use the A, B, C phase
      codes instead of s12N.

    """

    # No attributes defined for this class.


    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
