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
class LoadResponseCharacteristic(IdentifiedObject):
    """
    Models the characteristic response of the load demand due to changes in system conditions such as voltage and
      frequency. This is not related to demand response.  If LoadResponseCharacteristic.exponentModel is True, the
      voltage exponents are specified and used as to calculate:  Active power component = Pnominal *
      (Voltage/cim:BaseVoltage.nominalVoltage) ** cim:LoadResponseCharacteristic.pVoltageExponent  Reactive power
      component = Qnominal * (Voltage/cim:BaseVoltage.nominalVoltage)**
      cim:LoadResponseCharacteristic.qVoltageExponent  Where  * means "multiply" and ** is "raised to power of".

    EnergyConsumer: The set of loads that have the response characteristics.
    exponentModel: Indicates the exponential voltage dependency model is to be used.   If false, the coefficient model
      is to be used. The exponential voltage dependency model consist of the attributes -
      pVoltageExponent - qVoltageExponent. The coefficient model consist of the attributes -
      pConstantImpedance - pConstantCurrent - pConstantPower - qConstantImpedance - qConstantCurrent
      - qConstantPower. The sum of pConstantImpedance, pConstantCurrent and pConstantPower shall
      equal 1. The sum of qConstantImpedance, qConstantCurrent and qConstantPower shall equal 1.
    pConstantCurrent: Portion of active power load modeled as constant current.
    pConstantImpedance: Portion of active power load modeled as constant impedance.
    pConstantPower: Portion of active power load modeled as constant power.
    pFrequencyExponent: Exponent of per unit frequency effecting active power.
    pVoltageExponent: Exponent of per unit voltage effecting real power.
    qConstantCurrent: Portion of reactive power load modeled as constant current.
    qConstantImpedance: Portion of reactive power load modeled as constant impedance.
    qConstantPower: Portion of reactive power load modeled as constant power.
    qFrequencyExponent: Exponent of per unit frequency effecting reactive power.
    qVoltageExponent: Exponent of per unit voltage effecting reactive power.
    """

    # *Association not used*
    # Type M:0..n in CIM
    # EnergyConsumer : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]}) # noqa: E501

    exponentModel : bool = Field(default=False, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    pConstantCurrent : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    pConstantImpedance : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    pConstantPower : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    pFrequencyExponent : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    pVoltageExponent : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    qConstantCurrent : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    qConstantImpedance : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    qConstantPower : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    qFrequencyExponent : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 

    qVoltageExponent : float = Field(default=0.0, json_schema_extra={"in_profiles":[Profile.EQ, ]}) 



    @cached_property
    def possible_profiles(self)->set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return { Profile.EQ,  }
