from .OperationalLimit import OperationalLimit


class ApparentPowerLimit(OperationalLimit):
    """
    Apparent power limit.

    :value: The apparent power limit. Default: 0.0
    """

    cgmesProfile = OperationalLimit.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.EQ.value,
        ],
        "value": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class OperationalLimit: \n"
        + OperationalLimit.__doc__
    )

    def __init__(self, value=0.0, *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.value = value

    def __str__(self):
        str = "class=ApparentPowerLimit\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
