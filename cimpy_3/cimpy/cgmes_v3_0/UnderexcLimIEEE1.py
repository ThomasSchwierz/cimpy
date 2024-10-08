from .UnderexcitationLimiterDynamics import UnderexcitationLimiterDynamics


class UnderexcLimIEEE1(UnderexcitationLimiterDynamics):
    """
    Type UEL1 model which has a circular limit boundary when plotted in terms of machine reactive power vs. real power output. Reference: IEEE UEL1 421.5-2005, 10.1.

    :kur: UEL radius setting (<i>K</i><i><sub>UR</sub></i>).  Typical value = 1,95. Default: 0.0
    :kuc: UEL centre setting (<i>K</i><i><sub>UC</sub></i>).  Typical value = 1,38. Default: 0.0
    :kuf: UEL excitation system stabilizer gain (<i>K</i><i><sub>UF</sub></i>).  Typical value = 3,3. Default: 0.0
    :vurmax: UEL maximum limit for radius phasor magnitude (<i>V</i><i><sub>URMAX</sub></i>).  Typical value = 5,8. Default: 0.0
    :vucmax: UEL maximum limit for operating point phasor magnitude (<i>V</i><i><sub>UCMAX</sub></i>).  Typical value = 5,8. Default: 0.0
    :kui: UEL integral gain (<i>K</i><i><sub>UI</sub></i>).  Typical value = 0. Default: 0.0
    :kul: UEL proportional gain (<i>K</i><i><sub>UL</sub></i>).  Typical value = 100. Default: 0.0
    :vuimax: UEL integrator output maximum limit (<i>V</i><i><sub>UIMAX</sub></i>) (&gt; UnderexcLimIEEE1.vuimin). Default: 0.0
    :vuimin: UEL integrator output minimum limit (<i>V</i><i><sub>UIMIN</sub></i>) (&lt; UnderexcLimIEEE1.vuimax). Default: 0.0
    :tu1: UEL lead time constant (<i>T</i><i><sub>U1</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
    :tu2: UEL lag time constant (<i>T</i><i><sub>U2</sub></i>) (&gt;= 0).  Typical value = 0,05. Default: 0
    :tu3: UEL lead time constant (<i>T</i><i><sub>U3</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
    :tu4: UEL lag time constant (<i>T</i><i><sub>U4</sub></i>) (&gt;= 0).  Typical value = 0. Default: 0
    :vulmax: UEL output maximum limit (<i>V</i><i><sub>ULMAX</sub></i>) (&gt; UnderexcLimIEEE1.vulmin).  Typical value = 18. Default: 0.0
    :vulmin: UEL output minimum limit (<i>V</i><i><sub>ULMIN</sub></i>) (&lt; UnderexcLimIEEE1.vulmax).  Typical value = -18. Default: 0.0
    """

    cgmesProfile = UnderexcitationLimiterDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "kur": [
            cgmesProfile.DY.value,
        ],
        "kuc": [
            cgmesProfile.DY.value,
        ],
        "kuf": [
            cgmesProfile.DY.value,
        ],
        "vurmax": [
            cgmesProfile.DY.value,
        ],
        "vucmax": [
            cgmesProfile.DY.value,
        ],
        "kui": [
            cgmesProfile.DY.value,
        ],
        "kul": [
            cgmesProfile.DY.value,
        ],
        "vuimax": [
            cgmesProfile.DY.value,
        ],
        "vuimin": [
            cgmesProfile.DY.value,
        ],
        "tu1": [
            cgmesProfile.DY.value,
        ],
        "tu2": [
            cgmesProfile.DY.value,
        ],
        "tu3": [
            cgmesProfile.DY.value,
        ],
        "tu4": [
            cgmesProfile.DY.value,
        ],
        "vulmax": [
            cgmesProfile.DY.value,
        ],
        "vulmin": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class UnderexcitationLimiterDynamics: \n"
        + UnderexcitationLimiterDynamics.__doc__
    )

    def __init__(
        self,
        kur=0.0,
        kuc=0.0,
        kuf=0.0,
        vurmax=0.0,
        vucmax=0.0,
        kui=0.0,
        kul=0.0,
        vuimax=0.0,
        vuimin=0.0,
        tu1=0,
        tu2=0,
        tu3=0,
        tu4=0,
        vulmax=0.0,
        vulmin=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.kur = kur
        self.kuc = kuc
        self.kuf = kuf
        self.vurmax = vurmax
        self.vucmax = vucmax
        self.kui = kui
        self.kul = kul
        self.vuimax = vuimax
        self.vuimin = vuimin
        self.tu1 = tu1
        self.tu2 = tu2
        self.tu3 = tu3
        self.tu4 = tu4
        self.vulmax = vulmax
        self.vulmin = vulmin

    def __str__(self):
        str = "class=UnderexcLimIEEE1\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
