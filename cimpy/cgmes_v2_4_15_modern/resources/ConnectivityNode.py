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
class ConnectivityNode(IdentifiedObject):
    """
    Connectivity nodes are points where terminals of AC conducting equipment are connected together with zero impedance.

    Terminals: The connectivity node to which this terminal connects with zero impedance.
    ConnectivityNodeContainer: Container of this connectivity node.
    boundaryPoint: Identifies if a node is a BoundaryPoint. If boundaryPoint=true the ConnectivityNode or the
      TopologicalNode represents a BoundaryPoint.
    fromEndIsoCode: The attribute is used for an exchange of the ISO code of the region to which the `From` side of the
      Boundary point belongs to or it is connected to. The ISO code is two characters country code
      as defined by ISO 3166 (). The length of the string is 2 characters maximum. The attribute is
      a required for the Boundary Model Authority Set where this attribute is used only for the
      TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary
      Equipment profile.
    fromEndName: The attribute is used for an exchange of a human readable name with length of the string 32 characters
      maximum. The attribute covers two cases:  The attribute is required for the Boundary Model
      Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and
      ConnectivityNode in the Boundary Equipment profile.
    fromEndNameTso: The attribute is used for an exchange of the name of the TSO to which the `From` side of the
      Boundary point belongs to or it is connected to. The length of the string is 32 characters
      maximum. The attribute is required for the Boundary Model Authority Set where it is used only
      for the TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary
      Equipment profile.
    toEndIsoCode: The attribute is used for an exchange of the ISO code of the region to which the `To` side of the
      Boundary point belongs to or it is connected to. The ISO code is two characters country code as
      defined by ISO 3166 (). The length of the string is 2 characters maximum. The attribute is a
      required for the Boundary Model Authority Set where this attribute is used only for the
      TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment
      profile.
    toEndName: The attribute is used for an exchange of a human readable name with length of the string 32 characters
      maximum. The attribute covers two cases:  The attribute is required for the Boundary Model
      Authority Set where it is used only for the TopologicalNode in the Boundary Topology profile and
      ConnectivityNode in the Boundary Equipment profile.
    toEndNameTso: The attribute is used for an exchange of the name of the TSO to which the `To` side of the Boundary
      point belongs to or it is connected to. The length of the string is 32 characters maximum. The
      attribute is required for the Boundary Model Authority Set where it is used only for the
      TopologicalNode in the Boundary Topology profile and ConnectivityNode in the Boundary Equipment
      profile.
    TopologicalNode: The topological node to which this connectivity node is assigned.  May depend on the current state
      of switches in the network.
    """

    # *Association not used*
    # Type M:0..n in CIM
    # Terminals : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    ConnectivityNodeContainer : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, Profile.EQ_BD, ]}) 

    boundaryPoint : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.EQ_BD, ]}) 

    fromEndIsoCode : str = Field(default="", json_schema_extra={"in_profiles":[Profile.EQ_BD, ]}) 

    fromEndName : str = Field(default="", json_schema_extra={"in_profiles":[Profile.EQ_BD, ]}) 

    fromEndNameTso : str = Field(default="", json_schema_extra={"in_profiles":[Profile.EQ_BD, ]}) 

    toEndIsoCode : str = Field(default="", json_schema_extra={"in_profiles":[Profile.EQ_BD, ]}) 

    toEndName : str = Field(default="", json_schema_extra={"in_profiles":[Profile.EQ_BD, ]}) 

    toEndNameTso : str = Field(default="", json_schema_extra={"in_profiles":[Profile.EQ_BD, ]}) 

    TopologicalNode : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.TP_BD, Profile.TP, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ, Profile.EQ_BD, Profile.TP_BD, Profile.TP,  }
