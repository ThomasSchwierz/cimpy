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
class Date(Base):
    """
    Date as "yyyy-mm-dd", which conforms with ISO 8601. UTC time zone is specified as "yyyy-mm-ddZ". A local timezone
      relative UTC is specified as "yyyy-mm-dd(+/-)hh:mm".

    """

    # No attributes defined for this class.


    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY, Profile.DL, Profile.EQ, Profile.SV, Profile.EQ_BD, Profile.SSH, Profile.TP_BD, Profile.TP, Profile.GL,  }
