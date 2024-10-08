from .RegulatingControl import RegulatingControl


class TapChangerControl(RegulatingControl):
    """
    Describes behaviour specific to tap changers, e.g. how the voltage at the end of a line varies with the load level and compensation of the voltage drop by tap adjustment.

    :TapChanger: The tap changers that participates in this regulating tap control scheme. Default: "list"
    """

    cgmesProfile = RegulatingControl.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
        ],
        "TapChanger": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class RegulatingControl: \n"
        + RegulatingControl.__doc__
    )

    def __init__(self, TapChanger="list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.TapChanger = TapChanger

    def __str__(self):
        str = "class=TapChangerControl\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
