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
class TopologicalNode(IdentifiedObject):
    """
    For a detailed substation model a topological node is a set of connectivity nodes that, in the current network
      state, are connected together through any type of closed switches, including  jumpers. Topological nodes
      change as the current network state changes (i.e., switches, breakers, etc. change state). For a planning
      model, switch statuses are not used to form topological nodes. Instead they are manually created or deleted in
      a model builder tool. Topological nodes maintained this way are also called "busses".

    SvInjection: The topological node associated with the flow injection state variable.
    SvVoltage: The topological node associated with the voltage state.
    AngleRefTopologicalIsland: The island for which the node is an angle reference.   Normally there is one angle
      reference node for each island.
    TopologicalIsland: A topological node belongs to a topological island.
    BaseVoltage: The base voltage of the topologocial node.
    ConnectivityNodes: The connectivity nodes combine together to form this topological node.  May depend on the current
      state of switches in the network.
    ConnectivityNodeContainer: The connectivity node container to which the toplogical node belongs.
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
    ReportingGroup: The topological nodes that belong to the reporting group.
    Terminal: The topological node associated with the terminal.   This can be used as an alternative to the
      connectivity node path to topological node, thus making it unneccesary to model connectivity nodes
      in some cases.   Note that the if connectivity nodes are in the model, this association would
      probably not be used as an input specification.
    """

    # *Association not used*
    # Type M:0..1 in CIM
    # SvInjection : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.SV, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM
    # SvVoltage : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.SV, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM
    # AngleRefTopologicalIsland : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.SV, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM
    # TopologicalIsland : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.SV, ]}) # noqa: E501

    BaseVoltage : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.TP_BD, Profile.TP, ]}) 

    # *Association not used*
    # Type M:0..n in CIM
    # ConnectivityNodes : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.TP_BD, Profile.TP, ]}) # noqa: E501

    ConnectivityNodeContainer : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.TP_BD, Profile.TP, ]}) 

    boundaryPoint : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.TP_BD, ]}) 

    fromEndIsoCode : str = Field(default="", json_schema_extra={"in_profiles":[Profile.TP_BD, ]}) 

    fromEndName : str = Field(default="", json_schema_extra={"in_profiles":[Profile.TP_BD, ]}) 

    fromEndNameTso : str = Field(default="", json_schema_extra={"in_profiles":[Profile.TP_BD, ]}) 

    toEndIsoCode : str = Field(default="", json_schema_extra={"in_profiles":[Profile.TP_BD, ]}) 

    toEndName : str = Field(default="", json_schema_extra={"in_profiles":[Profile.TP_BD, ]}) 

    toEndNameTso : str = Field(default="", json_schema_extra={"in_profiles":[Profile.TP_BD, ]}) 

    ReportingGroup : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.TP, ]}) 

    # *Association not used*
    # Type M:0..n in CIM
    # Terminal : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.TP, ]}) # noqa: E501



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.SV, Profile.TP_BD, Profile.TP,  }
