from cimpy.cgmes_v2_4_15.Base import Base


class Conductance(Base):
    """
    Factor by which voltage must be multiplied to give corresponding power lost from a circuit. Real part of admittance.

    :value:  Default: 0.0
    :unit:  Default: None
    :multiplier:  Default: None
    """

    cgmesProfile = Base.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.EQ.value,
        ],
        "value": [
            cgmesProfile.EQ.value,
        ],
        "unit": [
            cgmesProfile.EQ.value,
        ],
        "multiplier": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    def __init__(
        self,
        value=0.0,
        unit=None,
        multiplier=None,
    ):

        self.value = value
        self.unit = unit
        self.multiplier = multiplier

    def __str__(self):
        str = "class=Conductance\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
