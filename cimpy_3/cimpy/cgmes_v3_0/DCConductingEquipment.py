from .Equipment import Equipment


class DCConductingEquipment(Equipment):
    """
    The parts of the DC power system that are designed to carry current or that are conductively connected through DC terminals.

    :ratedUdc: Rated DC device voltage. The attribute shall be a positive value. It is configuration data used in power flow. Default: 0.0
    :DCTerminals: A DC conducting equipment has DC terminals. Default: "list"
    """

    cgmesProfile = Equipment.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.EQ.value,
        ],
        "ratedUdc": [
            cgmesProfile.EQ.value,
        ],
        "DCTerminals": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += "\n Documentation of parent class Equipment: \n" + Equipment.__doc__

    def __init__(self, ratedUdc=0.0, DCTerminals="list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.ratedUdc = ratedUdc
        self.DCTerminals = DCTerminals

    def __str__(self):
        str = "class=DCConductingEquipment\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
