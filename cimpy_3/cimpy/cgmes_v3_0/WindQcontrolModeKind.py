from .Base import Base


class WindQcontrolModeKind(Base):
    """
    General wind turbine Q control modes <i>M</i><i><sub>qG</sub></i><i>.</i>

    """

    cgmesProfile = Base.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    def __init__(
        self,
    ):

        pass

    def __str__(self):
        str = "class=WindQcontrolModeKind\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
