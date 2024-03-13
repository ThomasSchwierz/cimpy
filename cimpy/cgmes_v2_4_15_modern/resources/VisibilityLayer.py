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
class VisibilityLayer(IdentifiedObject):
    """
    Layers are typically used for grouping diagram objects according to themes and scales. Themes are used to display or
      hide certain information (e.g., lakes, borders), while scales are used for hiding or displaying information
      depending on the current zoom level (hide text when it is too small to be read, or when it exceeds the screen
      size). This is also called de-cluttering.  CIM based graphics exchange will support an m:n relationship
      between diagram objects and layers. It will be the task of the importing system to convert an m:n case into an
      appropriate 1:n representation if the importing system does not support m:n.

    VisibleObjects: A visibility layer can contain one or more diagram objects.
    drawingOrder: The drawing order for this layer.  The higher the number, the later the layer and the objects within
      it are rendered.
    """

    VisibleObjects : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.DL, ]}) 

    drawingOrder : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DL, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DL,  }
