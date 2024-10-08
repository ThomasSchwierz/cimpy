from .SynchronousMachineDynamics import SynchronousMachineDynamics


class SynchronousMachineSimplified(SynchronousMachineDynamics):
    """
    The simplified model represents a synchronous generator as a constant internal voltage behind an impedance<i> </i>(<i>Rs + jXp</i>) as shown in the Simplified diagram. Since internal voltage is held constant, there is no <i>Efd</i> input and any excitation system model will be ignored.  There is also no <i>Ifd</i> output. This model should not be used for representing a real generator except, perhaps, small generators whose response is insignificant.   The parameters used for the simplified model include: - RotatingMachineDynamics.damping (<i>D</i>); - RotatingMachineDynamics.inertia (<i>H</i>); - RotatingMachineDynamics.statorLeakageReactance (used to exchange <i>jXp </i>for SynchronousMachineSimplified); - RotatingMachineDynamics.statorResistance (<i>Rs</i>).

    """

    cgmesProfile = SynchronousMachineDynamics.cgmesProfile

    possibleProfileList = {
        "class": [
            cgmesProfile.DY.value,
        ],
    }

    serializationProfile = {}

    __doc__ += (
        "\n Documentation of parent class SynchronousMachineDynamics: \n"
        + SynchronousMachineDynamics.__doc__
    )

    def __init__(self, *args, **kw_args):
        super().__init__(*args, **kw_args)

        pass

    def __str__(self):
        str = "class=SynchronousMachineSimplified\n"
        attributes = self.__dict__
        for key in attributes.keys():
            str = str + key + "={}\n".format(attributes[key])
        return str
