from .RegulatingCondEq import RegulatingCondEq


class StaticVarCompensator(RegulatingCondEq):
    """
    A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate in fixed MVar output mode or in voltage control mode. When in voltage control mode, the output of the SVC will be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage setpoint, the SVC MVar output is zero.

    :StaticVarCompensatorDynamics: Static Var Compensator dynamics model used to describe dynamic behaviour of this Static Var Compensator. Default: None
    :q: Reactive power injection. Load sign convention is used, i.e. positive sign means flow out from a node. Starting value for a steady state solution. Default: 0.0
    :capacitiveRating: Capacitive reactance at maximum capacitive reactive power.  Shall always be positive. Default: 0.0
    :inductiveRating: Inductive reactance at maximum inductive reactive power.  Shall always be negative. Default: 0.0
    :slope: The characteristics slope of an SVC defines how the reactive power output changes in proportion to the difference between the regulated bus voltage and the voltage setpoint. The attribute shall be a positive value or zero. Default: 0.0
    :sVCControlMode: SVC control mode. Default: None
    :voltageSetPoint: The reactive power output of the SVC is proportional to the difference between the voltage at the regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the voltage setpoint, the reactive power output is zero. Default: 0.0
    """

    cgmesProfile = RegulatingCondEq.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
            cgmesProfile.SSH.value,
            cgmesProfile.EQ.value,
        ],
        "StaticVarCompensatorDynamics": [
            cgmesProfile.DY.value,
        ],
        "q": [
            cgmesProfile.SSH.value,
        ],
        "capacitiveRating": [
            cgmesProfile.EQ.value,
        ],
        "inductiveRating": [
            cgmesProfile.EQ.value,
        ],
        "slope": [
            cgmesProfile.EQ.value,
        ],
        "sVCControlMode": [
            cgmesProfile.EQ.value,
        ],
        "voltageSetPoint": [
            cgmesProfile.EQ.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class RegulatingCondEq: \n"
        + RegulatingCondEq.__doc__
    )

    def __init__(
        self,
        StaticVarCompensatorDynamics=None,
        q=0.0,
        capacitiveRating=0.0,
        inductiveRating=0.0,
        slope=0.0,
        sVCControlMode=None,
        voltageSetPoint=0.0,
        *args,
        **kw_args,
    ):
        super().__init__(*args, **kw_args)

        self.StaticVarCompensatorDynamics = StaticVarCompensatorDynamics
        self.q = q
        self.capacitiveRating = capacitiveRating
        self.inductiveRating = inductiveRating
        self.slope = slope
        self.sVCControlMode = sVCControlMode
        self.voltageSetPoint = voltageSetPoint

    def __str__(self):
        str = "class=StaticVarCompensator\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
