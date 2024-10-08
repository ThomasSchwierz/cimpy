from .PFVArControllerType1Dynamics import PFVArControllerType1Dynamics


class PFVArType1IEEEPFController(PFVArControllerType1Dynamics):
    """
    IEEE PF controller type 1 which operates by moving the voltage reference directly. Reference: IEEE 421.5-2005, 11.2.

    :ovex: Overexcitation Flag (<i>OVEX</i>) true = overexcited false = underexcited. Default: False
    :tpfc: PF controller time delay (<i>T</i><i><sub>PFC</sub></i>) (&gt;= 0).  Typical value = 5. Default: 0
    :vitmin: Minimum machine terminal current needed to enable pf/var controller (<i>V</i><i><sub>ITMIN</sub></i>). Default: 0.0
    :vpf: Synchronous machine power factor (<i>V</i><i><sub>PF</sub></i>). Default: 0.0
    :vpfcbw: PF controller deadband (<i>V</i><i><sub>PFC_BW</sub></i>).  Typical value = 0,05. Default: 0.0
    :vpfref: PF controller reference (<i>V</i><i><sub>PFREF</sub></i>). Default: 0.0
    :vvtmax: Maximum machine terminal voltage needed for pf/var controller to be enabled (<i>V</i><i><sub>VTMAX</sub></i>) (&gt; PFVArType1IEEEPFController.vvtmin). Default: 0.0
    :vvtmin: Minimum machine terminal voltage needed to enable pf/var controller (<i>V</i><i><sub>VTMIN</sub></i>) (&lt; PFVArType1IEEEPFController.vvtmax). Default: 0.0
    """

    cgmesProfile = PFVArControllerType1Dynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "ovex": [
            cgmesProfile.DY.value,
        ],
        "tpfc": [
            cgmesProfile.DY.value,
        ],
        "vitmin": [
            cgmesProfile.DY.value,
        ],
        "vpf": [
            cgmesProfile.DY.value,
        ],
        "vpfcbw": [
            cgmesProfile.DY.value,
        ],
        "vpfref": [
            cgmesProfile.DY.value,
        ],
        "vvtmax": [
            cgmesProfile.DY.value,
        ],
        "vvtmin": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class PFVArControllerType1Dynamics: \n"
        + PFVArControllerType1Dynamics.__doc__
    )

    def __init__(
        self,
        ovex=False,
        tpfc=0,
        vitmin=0.0,
        vpf=0.0,
        vpfcbw=0.0,
        vpfref=0.0,
        vvtmax=0.0,
        vvtmin=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.ovex = ovex
        self.tpfc = tpfc
        self.vitmin = vitmin
        self.vpf = vpf
        self.vpfcbw = vpfcbw
        self.vpfref = vpfref
        self.vvtmax = vvtmax
        self.vvtmin = vvtmin

    def __str__(self):
        str = "class=PFVArType1IEEEPFController\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
