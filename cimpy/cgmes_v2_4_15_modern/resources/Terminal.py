"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .ACDCTerminal import ACDCTerminal

@dataclass
class Terminal(ACDCTerminal):
    """
    An AC electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection
      points called connectivity nodes.

    ConductingEquipment: The conducting equipment of the terminal.  Conducting equipment have  terminals that may be
      connected to other conducting equipment terminals via connectivity nodes or topological
      nodes.
    RemoteInputSignal: Input signal coming from this terminal.
    ConverterDCSides: Point of common coupling terminal for this converter DC side. It is typically the terminal on the
      power transformer (or switch) closest to the AC network. The power flow measurement must be
      the sum of all flows into the transformer.
    ConnectivityNode: Terminals interconnected with zero impedance at a this connectivity node.
    phases: Represents the normal network phasing condition. If the attribute is missing three phases (ABC or ABCN)
      shall be assumed.
    HasFirstMutualCoupling: Mutual couplings associated with the branch as the first branch.
    HasSecondMutualCoupling: Mutual couplings with the branch associated as the first branch.
    RegulatingControl: The terminal associated with this regulating control.  The terminal is associated instead of a
      node, since the terminal could connect into either a topological node (bus in bus-branch
      model) or a connectivity node (detailed switch model).  Sometimes it is useful to model
      regulation at a terminal of a bus bar object since the bus bar can be present in both a
      bus-branch model or a model with switch detail.
    TieFlow: The control area tie flows to which this terminal associates.
    TransformerEnd: All transformer ends connected at this terminal.
    SvPowerFlow: The power flow state variable associated with the terminal.
    TopologicalNode: The terminals associated with the topological node.   This can be used as an alternative to the
      connectivity node path to terminal, thus making it unneccesary to model connectivity nodes in
      some cases.   Note that if connectivity nodes are in the model, this association would
      probably not be used as an input specification.
    """

    ConductingEquipment : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, Profile.EQ, Profile.EQ_BD, ]}) 

    # *Association not used*
    # Type M:0..n in CIM
    # RemoteInputSignal : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DY, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..n in CIM
    # ConverterDCSides : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    ConnectivityNode : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    phases : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    # *Association not used*
    # Type M:0..n in CIM
    # HasFirstMutualCoupling : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..n in CIM
    # HasSecondMutualCoupling : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM
    # RegulatingControl : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..2 in CIM
    # TieFlow : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..n in CIM
    # TransformerEnd : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    # *Association not used*
    # Type M:0..1 in CIM
    # SvPowerFlow : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.SV, ]}) # noqa: E501

    TopologicalNode : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.TP, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY, Profile.EQ, Profile.SV, Profile.EQ_BD, Profile.SSH, Profile.TP,  }
