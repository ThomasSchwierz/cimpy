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
class TransformerEnd(IdentifiedObject):
    """
    A conducting connection point of a power transformer. It corresponds to a physical transformer winding terminal.  In
      earlier CIM versions, the TransformerWinding class served a similar purpose, but this class is more flexible
      because it associates to terminal but is not a specialization of ConductingEquipment.

    BaseVoltage: Base voltage of the transformer end.  This is essential for PU calculation.
    Terminal: Terminal of the power transformer to which this transformer end belongs.
    PhaseTapChanger: Transformer end to which this phase tap changer belongs.
    RatioTapChanger: Transformer end to which this ratio tap changer belongs.
    rground: (for Yn and Zn connections) Resistance part of neutral impedance where `grounded` is true.
    endNumber: Number for this transformer end, corresponding to the end`s order in the power transformer vector group
      or phase angle clock number.  Highest voltage winding should be 1.  Each end within a power
      transformer should have a unique subsequent end number.   Note the transformer end number need not
      match the terminal sequence number.
    grounded: (for Yn and Zn connections) True if the neutral is solidly grounded.
    xground: (for Yn and Zn connections) Reactive part of neutral impedance where `grounded` is true.
    """

    BaseVoltage : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    Terminal : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    # *Association not used*
    # Type M:0..1 in CIM
    # PhaseTapChanger : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM
    # RatioTapChanger : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    rground : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    endNumber : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    grounded : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    xground : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
