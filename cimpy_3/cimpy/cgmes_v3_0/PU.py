from .Base import Base


class PU(Base):
    """
    Per Unit - a positive or negative value referred to a defined base. Values typically range from -10 to +10.

    :value:  Default: 0.0
    :unit:  Default: None
    :multiplier:  Default: None
    """

    cgmesProfile = Base.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
            cgmesProfile.SSH.value,
            cgmesProfile.SC.value,
        ],
        "value": [
            cgmesProfile.DY.value,
            cgmesProfile.SSH.value,
            cgmesProfile.SC.value,
        ],
        "unit": [
            cgmesProfile.DY.value,
            cgmesProfile.SSH.value,
            cgmesProfile.SC.value,
        ],
        "multiplier": [
            cgmesProfile.DY.value,
            cgmesProfile.SSH.value,
            cgmesProfile.SC.value,
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
        str = "class=PU\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
