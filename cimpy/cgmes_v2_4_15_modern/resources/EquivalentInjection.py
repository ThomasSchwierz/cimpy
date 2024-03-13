"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .EquivalentEquipment import EquivalentEquipment

@dataclass
class EquivalentInjection(EquivalentEquipment):
    """
    This class represents equivalent injections (generation or load).  Voltage regulation is allowed only at the point
      of connection.

    ReactiveCapabilityCurve: The equivalent injection using this reactive capability curve.
    maxP: Maximum active power of the injection.
    maxQ: Used for modeling of infeed for load flow exchange. Not used for short circuit modeling.  If maxQ and minQ are
      not used ReactiveCapabilityCurve can be used.
    minP: Minimum active power of the injection.
    minQ: Used for modeling of infeed for load flow exchange. Not used for short circuit modeling.  If maxQ and minQ are
      not used ReactiveCapabilityCurve can be used.
    r: Positive sequence resistance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of
      network reduction prior to the data exchange.
    r0: Zero sequence resistance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of
      network reduction prior to the data exchange.
    r2: Negative sequence resistance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of
      network reduction prior to the data exchange.
    regulationCapability: Specifies whether or not the EquivalentInjection has the capability to regulate the local
      voltage.
    x: Positive sequence reactance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of
      network reduction prior to the data exchange.
    x0: Zero sequence reactance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of
      network reduction prior to the data exchange.
    x2: Negative sequence reactance. Used to represent Extended-Ward (IEC 60909). Usage : Extended-Ward is a result of
      network reduction prior to the data exchange.
    regulationStatus: Specifies the default regulation status of the EquivalentInjection.  True is regulating.  False is
      not regulating.
    regulationTarget: The target voltage for voltage regulation.
    p: Equivalent active power injection. Load sign convention is used, i.e. positive sign means flow out from a node.
      Starting value for steady state solutions.
    q: Equivalent reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node.
      Starting value for steady state solutions.
    """

    ReactiveCapabilityCurve : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    maxP : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    maxQ : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    minP : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    minQ : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    r : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    r0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    r2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    regulationCapability : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    x : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    x0 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    x2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    regulationStatus : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    regulationTarget : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    p : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    q : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.SSH, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ, Profile.SSH,  }
