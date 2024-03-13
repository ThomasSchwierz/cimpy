"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .TransformerEnd import TransformerEnd

@dataclass
class PowerTransformerEnd(TransformerEnd):
    """
    A PowerTransformerEnd is associated with each Terminal of a PowerTransformer. The impedance values r, r0, x, and x0
      of a PowerTransformerEnd represents a star equivalent as follows 1) for a two Terminal PowerTransformer the
      high voltage PowerTransformerEnd has non zero values on r, r0, x, and x0 while the low voltage
      PowerTransformerEnd has zero values for r, r0, x, and x0. 2) for a three Terminal PowerTransformer the three
      PowerTransformerEnds represents a star equivalent with each leg in the star represented by r, r0, x, and x0
      values. 3) for a PowerTransformer with more than three Terminals the PowerTransformerEnd impedance values
      cannot be used. Instead use the TransformerMeshImpedance or split the transformer into multiple
      PowerTransformers.

    PowerTransformer: The ends of this power transformer.
    b: Magnetizing branch susceptance (B mag).  The value can be positive or negative.
    connectionKind: Kind of connection.
    b0: Zero sequence magnetizing branch susceptance.
    phaseAngleClock: Terminal voltage phase angle displacement where 360 degrees are represented with clock hours. The
      valid values are 0 to 11. For example, for the secondary side end of a transformer with
      vector group code of `Dyn11`, specify the connection kind as wye with neutral and specify the
      phase angle of the clock as 11.  The clock value of the transformer end number specified as
      1, is assumed to be zero.  Note the transformer end number is not assumed to be the same as
      the terminal sequence number.
    ratedS: Normal apparent power rating. The attribute shall be a positive value. For a two-winding transformer the
      values for the high and low voltage sides shall be identical.
    g: Magnetizing branch conductance.
    ratedU: Rated voltage: phase-phase for three-phase windings, and either phase-phase or phase-neutral for single-
      phase windings. A high voltage side, as given by TransformerEnd.endNumber, shall have a ratedU that is
      greater or equal than ratedU for the lower voltage sides.
    g0: Zero sequence magnetizing branch conductance (star-model).
    r: Resistance (star-model) of the transformer end. The attribute shall be equal or greater than zero for non-
      equivalent transformers.
    r0: Zero sequence series resistance (star-model) of the transformer end.
    x: Positive sequence series reactance (star-model) of the transformer end.
    x0: Zero sequence series reactance of the transformer end.
    """

    PowerTransformer : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    b : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    connectionKind : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    b0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    phaseAngleClock : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    ratedS : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    g : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    ratedU : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    g0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    r : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    r0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    x : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    x0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
