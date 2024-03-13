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
class PFVArControllerType1UserDefined(PFVArControllerType1Dynamics):
    """
    Power Factor or VAr controller Type I function block whose dynamic behaviour is described by

    proprietary: Behaviour is based on proprietary model as opposed to detailed model. true = user-defined model is
      proprietary with behaviour mutually understood by sending and receiving applications and
      parameters passed as general attributes false = user-defined model is explicitly defined in terms
      of control blocks and their input and output signals.
    ProprietaryParameterDynamics: Parameter of this proprietary user-defined model.
    """

    proprietary : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    # *Association not used*
    # Type M:0..n in CIM
    # ProprietaryParameterDynamics : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
