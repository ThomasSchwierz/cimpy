from .Curve import Curve


class VsCapabilityCurve(Curve):
    """
    The P-Q capability curve for a voltage source converter, with P on X-axis and Qmin and Qmax on Y1-axis and Y2-axis.

    :VsConverterDCSides: All converters with this capability curve. Default: "list"
    """

    cgmesProfile = Curve.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.EQ.value,
        ],
        "VsConverterDCSides": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += "\n Documentation of parent class Curve: \n" + Curve.__doc__

    def __init__(self, VsConverterDCSides="list", *args, **kw_args):
        super().__init__(*args, **kw_args)

        self.VsConverterDCSides = VsConverterDCSides

    def __str__(self):
        str = "class=VsCapabilityCurve\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
