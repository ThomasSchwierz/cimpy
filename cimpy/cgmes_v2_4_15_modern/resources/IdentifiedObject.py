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
class IdentifiedObject(Base):
    """
    This is a root class to provide common identification for all classes needing identification and naming attributes.

    description: The description is a free human readable text describing or naming the object. It may be non unique and
      may not correlate to a naming hierarchy.
    mRID: Master resource identifier issued by a model authority. The mRID is globally unique within an exchange
      context. Global uniqueness is easily achieved by using a UUID,  as specified in RFC 4122, for the mRID.
      The use of UUID is strongly recommended. For CIMXML data files in RDF syntax conforming to IEC 61970-552
      Edition 1, the mRID is mapped to rdf:ID or rdf:about attributes that identify CIM object elements.
    name: The name is any free human readable and possibly non unique text naming the object.
    DiagramObjects: The domain object to which this diagram object is associated.
    energyIdentCodeEic: The attribute is used for an exchange of the EIC code (Energy identification Code). The length
      of the string is 16 characters as defined by the EIC code. References:
    shortName: The attribute is used for an exchange of a human readable short name with length of the string 12
      characters maximum.
    """

    description : str = Field(default="", json_schema_extra={"in_profiles":[Profile.DY, Profile.EQ, Profile.EQ_BD, Profile.TP_BD, Profile.TP, ]}) 

    mRID : str = Field(default="", json_schema_extra={"in_profiles":[Profile.DY, Profile.DL, Profile.EQ, Profile.SV, Profile.EQ_BD, Profile.SSH, Profile.TP_BD, Profile.TP, Profile.GL, ]}) 

    name : str = Field(default="", json_schema_extra={"in_profiles":[Profile.DY, Profile.DL, Profile.EQ, Profile.SV, Profile.EQ_BD, Profile.SSH, Profile.TP_BD, Profile.TP, Profile.GL, ]}) 

    # *Association not used*
    # Type M:0..n in CIM
    # DiagramObjects : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DL, ]}) # noqa: E501

    energyIdentCodeEic : str = Field(default="", json_schema_extra={"in_profiles":[Profile.EQ, Profile.EQ_BD, Profile.TP_BD, Profile.TP, ]}) 

    shortName : str = Field(default="", json_schema_extra={"in_profiles":[Profile.EQ, Profile.EQ_BD, Profile.TP_BD, Profile.TP, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY, Profile.DL, Profile.EQ, Profile.SV, Profile.EQ_BD, Profile.SSH, Profile.TP_BD, Profile.TP, Profile.GL,  }
