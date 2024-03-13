"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics

@dataclass
class PssIEEE4B(PowerSystemStabilizerDynamics):
    """
    The class represents IEEE Std 421.5-2005 type PSS2B power system stabilizer model. The PSS4B model represents a
      structure based on multiple working frequency bands. Three separate bands, respectively dedicated to the low-,
      intermediate- and high-frequency modes of oscillations, are used in this delta-omega (speed input) PSS.
      Reference: IEEE 4B 421.5-2005 Section 8.4.

    bwh1: Notch filter 1 (high-frequency band): Three dB bandwidth (B).
    bwh2: Notch filter 2 (high-frequency band): Three dB bandwidth (B).
    bwl1: Notch filter 1 (low-frequency band): Three dB bandwidth (B).
    bwl2: Notch filter 2 (low-frequency band): Three dB bandwidth (B).
    kh: High band gain (K).  Typical Value = 120.
    kh1: High band differential filter gain (K).  Typical Value = 66.
    kh11: High band first lead-lag blocks coefficient (K).  Typical Value = 1.
    kh17: High band first lead-lag blocks coefficient (K).  Typical Value = 1.
    kh2: High band differential filter gain (K).  Typical Value = 66.
    ki: Intermediate band gain (K).  Typical Value = 30.
    ki1: Intermediate band differential filter gain (K).  Typical Value = 66.
    ki11: Intermediate band first lead-lag blocks coefficient (K).  Typical Value = 1.
    ki17: Intermediate band first lead-lag blocks coefficient (K).  Typical Value = 1.
    ki2: Intermediate band differential filter gain (K).  Typical Value = 66.
    kl: Low band gain (K).  Typical Value = 7.5.
    kl1: Low band differential filter gain (K).  Typical Value = 66.
    kl11: Low band first lead-lag blocks coefficient (K).  Typical Value = 1.
    kl17: Low band first lead-lag blocks coefficient (K).  Typical Value = 1.
    kl2: Low band differential filter gain (K).  Typical Value = 66.
    omeganh1: Notch filter 1 (high-frequency band): filter frequency (omega).
    omeganh2: Notch filter 2 (high-frequency band): filter frequency (omega).
    omeganl1: Notch filter 1 (low-frequency band): filter frequency (omega).
    omeganl2: Notch filter 2 (low-frequency band): filter frequency (omega).
    th1: High band time constant (T).  Typical Value = 0.01513.
    th10: High band time constant (T).  Typical Value = 0.
    th11: High band time constant (T).  Typical Value = 0.
    th12: High band time constant (T).  Typical Value = 0.
    th2: High band time constant (T).  Typical Value = 0.01816.
    th3: High band time constant (T).  Typical Value = 0.
    th4: High band time constant (T).  Typical Value = 0.
    th5: High band time constant (T).  Typical Value = 0.
    th6: High band time constant (T).  Typical Value = 0.
    th7: High band time constant (T).  Typical Value = 0.01816.
    th8: High band time constant (T).  Typical Value = 0.02179.
    th9: High band time constant (T).  Typical Value = 0.
    ti1: Intermediate band time constant (T).  Typical Value = 0.173.
    ti10: Intermediate band time constant (T).  Typical Value = 0.
    ti11: Intermediate band time constant (T).  Typical Value = 0.
    ti12: Intermediate band time constant (T).  Typical Value = 0.
    ti2: Intermediate band time constant (T).  Typical Value = 0.2075.
    ti3: Intermediate band time constant (T).  Typical Value = 0.
    ti4: Intermediate band time constant (T).  Typical Value = 0.
    ti5: Intermediate band time constant (T).  Typical Value = 0.
    ti6: Intermediate band time constant (T).  Typical Value = 0.
    ti7: Intermediate band time constant (T).  Typical Value = 0.2075.
    ti8: Intermediate band time constant (T).  Typical Value = 0.2491.
    ti9: Intermediate band time constant (T).  Typical Value = 0.
    tl1: Low band time constant (T).  Typical Value = 1.73.
    tl10: Low band time constant (T).  Typical Value = 0.
    tl11: Low band time constant (T).  Typical Value = 0.
    tl12: Low band time constant (T).  Typical Value = 0.
    tl2: Low band time constant (T).  Typical Value = 2.075.
    tl3: Low band time constant (T).  Typical Value = 0.
    tl4: Low band time constant (T).  Typical Value = 0.
    tl5: Low band time constant (T).  Typical Value = 0.
    tl6: Low band time constant (T).  Typical Value = 0.
    tl7: Low band time constant (T).  Typical Value = 2.075.
    tl8: Low band time constant (T).  Typical Value = 2.491.
    tl9: Low band time constant (T).  Typical Value = 0.
    vhmax: High band output maximum limit (V).  Typical Value = 0.6.
    vhmin: High band output minimum limit (V).  Typical Value = -0.6.
    vimax: Intermediate band output maximum limit (V).  Typical Value = 0.6.
    vimin: Intermediate band output minimum limit (V).  Typical Value = -0.6.
    vlmax: Low band output maximum limit (V).  Typical Value = 0.075.
    vlmin: Low band output minimum limit (V).  Typical Value = -0.075.
    vstmax: PSS output maximum limit (V).  Typical Value = 0.15.
    vstmin: PSS output minimum limit (V).  Typical Value = -0.15.
    """

    bwh1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    bwh2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    bwl1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    bwl2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kh : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kh1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kh11 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kh17 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kh2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ki : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ki1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ki11 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ki17 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ki2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kl : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kl1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kl11 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kl17 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kl2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    omeganh1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    omeganh2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    omeganl1 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    omeganl2 : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    th1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    th10 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    th11 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    th12 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    th2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    th3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    th4 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    th5 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    th6 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    th7 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    th8 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    th9 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ti1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ti10 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ti11 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ti12 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ti2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ti3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ti4 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ti5 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ti6 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ti7 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ti8 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    ti9 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tl1 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tl10 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tl11 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tl12 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tl2 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tl3 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tl4 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tl5 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tl6 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tl7 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tl8 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tl9 : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vhmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vhmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vimax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vimin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vlmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vlmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vstmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vstmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
