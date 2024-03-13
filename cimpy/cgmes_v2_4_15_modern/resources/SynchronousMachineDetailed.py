"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .SynchronousMachineDynamics import SynchronousMachineDynamics

@dataclass
class SynchronousMachineDetailed(SynchronousMachineDynamics):
    """
    All synchronous machine detailed types use a subset of the same data parameters and input/output variables.   The
      several variations differ in the following ways:   It is not necessary for each simulation tool to have
      separate models for each of the model types.  The same model can often be used for several types by
      alternative logic within the model.  Also, differences in saturation representation may not result in
      significant model performance differences so model substitutions are often acceptable.

    saturationFactorQAxis: Q-axis saturation factor at rated terminal voltage (S1q) (>= 0). Typical Value = 0.02.
    saturationFactor120QAxis: Q-axis saturation factor at 120% of rated terminal voltage (S12q) (>=S1q).  Typical Value
      = 0.12.
    efdBaseRatio: Ratio of Efd bases of exciter and generator models.  Typical Value = 1.
    ifdBaseType: Excitation base system mode.  Typical Value = ifag.
    ifdBaseValue: Ifd base current if .ifdBaseType = other. Not needed if .ifdBaseType not = other.   Unit = A.  Typical
      Value = 0.
    """

    saturationFactorQAxis : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    saturationFactor120QAxis : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    efdBaseRatio : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ifdBaseType : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ifdBaseValue : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
