from .TurbineGovernorDynamics import TurbineGovernorDynamics


class GovSteam0(TurbineGovernorDynamics):
    """
    A simplified steam turbine governor.

    :mwbase: Base for power values (<i>MWbase</i>) (&gt; 0).  Unit = MW. Default: 0.0
    :r: Permanent droop (<i>R</i>).  Typical value = 0,05. Default: 0.0
    :t1: Steam bowl time constant (<i>T1</i>) (&gt; 0).  Typical value = 0,5. Default: 0
    :vmax: Maximum valve position, PU of <i>mwcap</i> (<i>Vmax</i>) (&gt; GovSteam0.vmin).  Typical value = 1. Default: 0.0
    :vmin: Minimum valve position, PU of <i>mwcap</i> (<i>Vmin</i>) (&lt; GovSteam0.vmax).  Typical value = 0. Default: 0.0
    :t2: Numerator time constant of <i>T2</i>/<i>T3</i> block (<i>T2</i>) (&gt;= 0).  Typical value = 3. Default: 0
    :t3: Reheater time constant (<i>T3</i>) (&gt; 0).  Typical value = 10. Default: 0
    :dt: Turbine damping coefficient (<i>Dt</i>).  Unit = delta P / delta speed. Typical value = 0. Default: 0.0
    """

    cgmesProfile = TurbineGovernorDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "mwbase": [
            cgmesProfile.DY.value,
        ],
        "r": [
            cgmesProfile.DY.value,
        ],
        "t1": [
            cgmesProfile.DY.value,
        ],
        "vmax": [
            cgmesProfile.DY.value,
        ],
        "vmin": [
            cgmesProfile.DY.value,
        ],
        "t2": [
            cgmesProfile.DY.value,
        ],
        "t3": [
            cgmesProfile.DY.value,
        ],
        "dt": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class TurbineGovernorDynamics: \n"
        + TurbineGovernorDynamics.__doc__
    )

    def __init__(
        self,
        mwbase=0.0,
        r=0.0,
        t1=0,
        vmax=0.0,
        vmin=0.0,
        t2=0,
        t3=0,
        dt=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.mwbase = mwbase
        self.r = r
        self.t1 = t1
        self.vmax = vmax
        self.vmin = vmin
        self.t2 = t2
        self.t3 = t3
        self.dt = dt

    def __str__(self):
        str = "class=GovSteam0\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
