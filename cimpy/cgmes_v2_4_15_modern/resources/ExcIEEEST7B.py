"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.profile import BaseProfile, Profile

from .ExcitationSystemDynamics import ExcitationSystemDynamics

@dataclass
class ExcIEEEST7B(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type ST7B model. This model is representative of static potential-source
      excitation systems. In this system, the AVR consists of a PI voltage regulator. A phase lead-lag filter in
      series allows introduction of a derivative function, typically used with brushless excitation systems. In that
      case, the regulator is of the PID type. In addition, the terminal voltage channel includes a phase lead-lag
      filter.  The AVR includes the appropriate inputs on its reference for overexcitation limiter (OEL1),
      underexcitation limiter (UEL), stator current limiter (SCL), and current compensator (DROOP). All these
      limitations, when they work at voltage reference level, keep the PSS (VS signal from Type PSS1A, PSS2A, or
      PSS2B) in operation. However, the UEL limitation can also be transferred to the high value (HV) gate acting on
      the output signal. In addition, the output signal passes through a low value (LV) gate for a ceiling
      overexcitation limiter (OEL2).  Reference: IEEE Standard 421.5-2005 Section 7.7.

    kh: High-value gate feedback gain (K).  Typical Value 1.
    kia: Voltage regulator integral gain (K).  Typical Value = 1.
    kl: Low-value gate feedback gain (K).  Typical Value 1.
    kpa: Voltage regulator proportional gain (K).  Typical Value = 40.
    oelin: OEL input selector (OELin). Typical Value = noOELinput.
    tb: Regulator lag time constant (T).  Typical Value 1.
    tc: Regulator lead time constant (T).  Typical Value 1.
    tf: Excitation control system stabilizer time constant (T).  Typical Value 1.
    tg: Feedback time constant of inner loop field voltage regulator (T). Typical Value 1.
    tia: Feedback time constant (T).  Typical Value = 3.
    uelin: UEL input selector (UELin). Typical Value = noUELinput.
    vmax: Maximum voltage reference signal (V).  Typical Value = 1.1.
    vmin: Minimum voltage reference signal (V).  Typical Value = 0.9.
    vrmax: Maximum voltage regulator output (V).  Typical Value = 5.
    vrmin: Minimum voltage regulator output (V).  Typical Value = -4.5.
    """

    kh : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kia : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kl : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    kpa : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    oelin : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tb : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tc : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tf : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tg : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    tia : int = Field(default=0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    uelin : Optional[str] = Field(default=None, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmax : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 

    vrmin : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.DY, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.DY,  }
