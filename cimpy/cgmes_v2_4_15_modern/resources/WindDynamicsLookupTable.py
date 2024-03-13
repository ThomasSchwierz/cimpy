"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .IdentifiedObject import IdentifiedObject

@dataclass
class WindDynamicsLookupTable(IdentifiedObject):
    """
    The class models a look up table for the purpose of wind standard models.

    WindContCurrLimIEC: The wind dynamics lookup table associated with this current control limitation model.
    WindContPType3IEC: The wind dynamics lookup table associated with this P control type 3 model.
    WindContRotorRIEC: The rotor resistance control model with which this wind dynamics lookup table is associated.
    input: Input value (x) for the lookup table function.
    lookupTableFunctionType: Type of the lookup table function.
    output: Output value (y) for the lookup table function.
    sequence: Sequence numbers of the pairs of the input (x) and the output (y) of the lookup table function.
    WindPlantFreqPcontrolIEC: The wind dynamics lookup table associated with this frequency and active power wind plant
      model.
    """

    WindContCurrLimIEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    WindContPType3IEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    WindContRotorRIEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    input : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    lookupTableFunctionType : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    output : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    sequence : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    WindPlantFreqPcontrolIEC : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
