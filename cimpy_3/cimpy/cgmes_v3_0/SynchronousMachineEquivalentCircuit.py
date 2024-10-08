from .SynchronousMachineDetailed import SynchronousMachineDetailed


class SynchronousMachineEquivalentCircuit(SynchronousMachineDetailed):
    """
    The electrical equations for all variations of the synchronous models are based on the SynchronousEquivalentCircuit diagram for the direct- and quadrature- axes. Equations for conversion between equivalent circuit and time constant reactance forms: <i>Xd</i> = <i>Xad </i>+<i> Xl</i> <i>X'd</i> = <i>Xl</i> + <i>Xad</i> x <i>Xfd</i> / (<i>Xad</i> + <i>Xfd</i>) <i>X"d</i> = <i>Xl</i> + <i>Xad</i> x <i>Xfd</i> x <i>X1d</i> / (<i>Xad</i> x <i>Xfd</i> + <i>Xad</i> x <i>X1d</i> + <i>Xfd</i> x <i>X1d</i>) <i>Xq</i> = <i>Xaq</i> + <i>Xl</i> <i>X'q</i> = <i>Xl</i> + <i>Xaq</i> x <i>X1q</i> / (<i>Xaq</i> + <i>X1q</i>) <i>X"q</i> = <i>Xl</i> + <i>Xaq</i> x <i>X1q</i> x <i>X2q</i> / (<i>Xaq</i> x <i>X1q</i> + <i>Xaq</i> x <i>X2q</i> + <i>X1q</i> x <i>X2q</i>) <i>T'do</i> = (<i>Xad</i> + <i>Xfd</i>) / (<i>omega</i><i><sub>0</sub></i> x <i>Rfd</i>) <i>T"do</i> = (<i>Xad</i> x <i>Xfd</i> + <i>Xad</i> x <i>X1d</i> + <i>Xfd</i> x <i>X1d</i>) / (<i>omega</i><i><sub>0</sub></i> x <i>R1d</i> x (<i>Xad</i> + <i>Xfd</i>) <i>T'qo</i> = (<i>Xaq</i> + <i>X1q</i>) / (<i>omega</i><i><sub>0</sub></i> x <i>R1q</i>) <i>T"qo</i> = (<i>Xaq</i> x <i>X1q</i> + <i>Xaq</i> x <i>X2q</i> + <i>X1q</i> x <i>X2q</i>) / (<i>omega</i><i><sub>0</sub></i> x <i>R2q</i> x (<i>Xaq</i> + <i>X1q</i>) Same equations using CIM attributes from SynchronousMachineTimeConstantReactance class on left of "=" and SynchronousMachineEquivalentCircuit class on right (except as noted): xDirectSync = xad + RotatingMachineDynamics.statorLeakageReactance xDirectTrans = RotatingMachineDynamics.statorLeakageReactance + xad x xfd / (xad + xfd) xDirectSubtrans = RotatingMachineDynamics.statorLeakageReactance + xad x xfd x x1d / (xad x xfd + xad x x1d + xfd x x1d) xQuadSync = xaq + RotatingMachineDynamics.statorLeakageReactance xQuadTrans = RotatingMachineDynamics.statorLeakageReactance + xaq x x1q / (xaq+ x1q) xQuadSubtrans = RotatingMachineDynamics.statorLeakageReactance + xaq x x1q x x2q / (xaq x x1q + xaq x x2q + x1q x x2q)  tpdo = (xad + xfd) / (2 x pi x nominal frequency x rfd) tppdo = (xad x xfd + xad x x1d + xfd x x1d) / (2 x pi x nominal frequency x r1d x (xad + xfd) tpqo = (xaq + x1q) / (2 x pi x nominal frequency x r1q) tppqo = (xaq x x1q + xaq x x2q + x1q x x2q) / (2 x pi x nominal frequency x r2q x (xaq + x1q) These are only valid for a simplified model where "Canay" reactance is zero.

    :xad: Direct-axis mutual reactance. Default: 0.0
    :rfd: Field winding resistance. Default: 0.0
    :xfd: Field winding leakage reactance. Default: 0.0
    :r1d: Direct-axis damper 1 winding resistance. Default: 0.0
    :x1d: Direct-axis damper 1 winding leakage reactance. Default: 0.0
    :xf1d: Differential mutual (`Canay`) reactance. Default: 0.0
    :xaq: Quadrature-axis mutual reactance. Default: 0.0
    :r1q: Quadrature-axis damper 1 winding resistance. Default: 0.0
    :x1q: Quadrature-axis damper 1 winding leakage reactance. Default: 0.0
    :r2q: Quadrature-axis damper 2 winding resistance. Default: 0.0
    :x2q: Quadrature-axis damper 2 winding leakage reactance. Default: 0.0
    """

    cgmesProfile = SynchronousMachineDetailed.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
        "xad": [
            cgmesProfile.DY.value,
        ],
        "rfd": [
            cgmesProfile.DY.value,
        ],
        "xfd": [
            cgmesProfile.DY.value,
        ],
        "r1d": [
            cgmesProfile.DY.value,
        ],
        "x1d": [
            cgmesProfile.DY.value,
        ],
        "xf1d": [
            cgmesProfile.DY.value,
        ],
        "xaq": [
            cgmesProfile.DY.value,
        ],
        "r1q": [
            cgmesProfile.DY.value,
        ],
        "x1q": [
            cgmesProfile.DY.value,
        ],
        "r2q": [
            cgmesProfile.DY.value,
        ],
        "x2q": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class SynchronousMachineDetailed: \n"
        + SynchronousMachineDetailed.__doc__
    )

    def __init__(
        self,
        xad=0.0,
        rfd=0.0,
        xfd=0.0,
        r1d=0.0,
        x1d=0.0,
        xf1d=0.0,
        xaq=0.0,
        r1q=0.0,
        x1q=0.0,
        r2q=0.0,
        x2q=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.xad = xad
        self.rfd = rfd
        self.xfd = xfd
        self.r1d = r1d
        self.x1d = x1d
        self.xf1d = xf1d
        self.xaq = xaq
        self.r1q = r1q
        self.x1q = x1q
        self.r2q = r2q
        self.x2q = x2q

    def __str__(self):
        str = "class=SynchronousMachineEquivalentCircuit\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
