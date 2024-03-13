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
class SteadyStateHypothesisVersion(Base):
    """
    Version details.

    baseUML: Base UML provided by CIM model manager.
    baseURI: Profile URI used in the Model Exchange header and defined in IEC standards.  It uniquely identifies the
      Profile and its version. It is given for information only and to identify the closest IEC profile to
      which this CGMES profile is based on.
    date: Profile creation date Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05.
    differenceModelURI: Difference model URI defined by IEC 61970-552.
    entsoeUML: UML provided by ENTSO-E.
    entsoeURI: Profile URI defined by ENTSO-E and used in the Model Exchange header.  It uniquely identifies the Profile
      and its version. The last two elements in the URI
      (http://entsoe.eu/CIM/SteadyStateHypothesis/yy/zzz) indicate major and minor versions where:  - yy
      - indicates a major version; - zzz - indicates a minor version.
    modelDescriptionURI: Model Description URI defined by IEC 61970-552.
    namespaceRDF: RDF namespace.
    namespaceUML: CIM UML namespace.
    shortName: The short name of the profile used in profile documentation.
    """

    baseUML : str = Field(default="", json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    baseURI : str = Field(default="", json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    date : str = Field(default="", json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    differenceModelURI : str = Field(default="", json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    entsoeUML : str = Field(default="", json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    entsoeURI : str = Field(default="", json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    modelDescriptionURI : str = Field(default="", json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    namespaceRDF : str = Field(default="", json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    namespaceUML : str = Field(default="", json_schema_extra={"in_profiles":[Profile.SSH, ]}) 

    shortName : str = Field(default="", json_schema_extra={"in_profiles":[Profile.SSH, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.SSH,  }
